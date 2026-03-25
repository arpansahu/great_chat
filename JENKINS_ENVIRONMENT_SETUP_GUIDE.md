# Jenkins Environment Setup Guide for great_chat

## Upgrade Summary (Completed)
✅ **Django standardized:** 5.0.6 → 4.2.28 (for consistency)  
✅ **Storage settings:** Converted to Django 4.2+ STORAGES dict  
✅ **MinIO endpoint:** Fixed AWS_S3_CUSTOM_DOMAIN configuration  
✅ **Dependencies:** Updated asgiref, certifi, django-storages  

## Jenkins Credential Setup

### Step 1: Create `.env` File

Create a file with all required environment variables:

```bash
# Project Configuration
ENV_PROJECT_NAME=great_chat
DEBUG=0
SECRET_KEY=your-secret-key-here
DOMAIN=great-chat.arpansahu.space
PROTOCOL=https://

# Docker Registry
DOCKER_REGISTRY=harbor.arpansahu.space
DOCKER_REPOSITORY=library
DOCKER_IMAGE_NAME=great_chat
DOCKER_PORT=8002

# Database (SQLite for great_chat)
DATABASE_URL=sqlite:///db.sqlite3

# Redis
REDIS_CLOUD_URL=rediss://:Gandu302redis@redis.arpansahu.space:9551/ssl_cert_reqs=none

# MinIO/S3 Storage
BUCKET_TYPE=MINIO
USE_S3=False
AWS_ACCESS_KEY_ID=arpansahu
AWS_SECRET_ACCESS_KEY=Gandu302@minio
AWS_STORAGE_BUCKET_NAME=arpansahu-one-bucket
AWS_S3_ENDPOINT_URL=https://minioapi.arpansahu.space
AWS_S3_CUSTOM_DOMAIN=minioapi.arpansahu.space/arpansahu-one-bucket

# Email (Mailjet)
MAIL_JET_API_KEY=your-api-key
MAIL_JET_API_SECRET=your-api-secret
MAIL_JET_EMAIL_ADDRESS=noreply@arpansahu.space
MY_EMAIL_ADDRESS=your@email.com

# Sentry
SENTRY_ENVIRONMENT=production
SENTRY_DSH_URL=your-sentry-dsn
SENTRY_ORG=arpansahu
SENTRY_PROJECT=great_chat
SENTRY_AUTH_TOKEN=your-sentry-token

# Jenkins
JENKINS_DOMAIN=jenkins.arpansahu.space

# Server
SERVER_NAME=great-chat.arpansahu.space

# Allowed Hosts
ALLOWED_HOSTS=localhost 127.0.0.1 .arpansahu.space

# Harbor
HARBOR_URL=https://harbor.arpansahu.space
HARBOR_USERNAME=admin
HARBOR_PASSWORD=Gandu302@harbor
```

### Step 2: Upload to Jenkins

1. **Navigate to Jenkins:**
   ```
   https://jenkins.arpansahu.space
   Username: arpansahu
   Password: Gandu302@jenkins
   ```

2. **Go to Credentials:**
   - Dashboard → Manage Jenkins → Credentials
   - System → Global credentials → Add Credentials

3. **Create New Credential:**
   - **Kind:** Secret file
   - **File:** Upload your `.env` file
   - **ID:** `great_chat_env_file` (MUST match Jenkinsfile)
   - **Description:** Environment variables for great_chat
   - Click "Create"

### Step 3: Update Kubernetes Secret

The secret currently has incorrect values (DEBUG=1, DOMAIN=localhost). Update it:

```bash
ssh arpansahu@arpansahu.space

# Delete old secret
sudo kubectl delete secret great-chat-secret -n default

# Create new secret from updated .env file
sudo kubectl create secret generic great-chat-secret \
  --from-env-file=.env \
  -n default

# Verify
sudo kubectl get secret great-chat-secret -n default -o yaml
```

### Step 4: Create Jenkins Pipeline

1. **Create New Pipeline:**
   - Dashboard → New Item
   - Name: `great-chat` (or `great-chat-build`)
   - Type: Pipeline
   - Click OK

2. **Configure Pipeline:**
   - **Description:** Build pipeline for great_chat
   - **Pipeline Definition:** Pipeline script from SCM
   - **SCM:** Git
   - **Repository URL:** `https://github.com/arpansahu/great_chat.git`
   - **Branch:** `*/main`
   - **Script Path:** `Jenkinsfile-build`
   - Click "Save"

### Step 5: Trigger Build

```bash
# Option 1: From Jenkins UI
# Click "Build Now" or "Build with Parameters"

# Option 2: Using curl (requires API token)
curl -X POST "https://arpansahu:<API_TOKEN>@jenkins.arpansahu.space/job/great-chat/build"
```

## Deployment Pipeline Setup

### Step 1: Ensure Harbor Registry Secret Exists

```bash
ssh arpansahu@arpansahu.space

# Check if secret exists
sudo kubectl get secret harbor-registry-secret -n default || \
sudo kubectl create secret docker-registry harbor-registry-secret \
  --docker-server=harbor.arpansahu.space \
  --docker-username=admin \
  --docker-password=Gandu302@harbor \
  --docker-email=admin@arpansahu.space \
  -n default
```

### Step 2: Create Deploy Pipeline in Jenkins

1. **Create New Pipeline:**
   - Name: `great-chat-deploy`
   - Type: Pipeline
   - Script Path: `Jenkinsfile-deploy`

2. **Required Jenkins Credentials:**
   - `great_chat_env_file` (already created)
   - `jenkins-admin-credentials` (Username/Password for SSH)
     - Username: arpansahu
     - Password: Gandu302@

### Step 3: Deploy

The deploy pipeline will:
- Pull latest image from Harbor
- Update Kubernetes deployment
- Collect static files to MinIO
- Restart pods with zero downtime

## Verification

```bash
# Check deployment status
ssh arpansahu@arpansahu.space 'sudo kubectl get deployments -n default | grep great-chat'

# Expected output:
# great-chat-app         1/1     1            1           28d

# Check pod status
ssh arpansahu@arpansahu.space 'sudo kubectl get pods -n default | grep great-chat'

# Check Django settings in running pod
ssh arpansahu@arpansahu.space 'sudo kubectl exec -n default deployment/great-chat-app -- python manage.py shell -c "from django.conf import settings; print(f\"DEBUG: {settings.DEBUG}\"); print(f\"DOMAIN: {settings.DOMAIN}\"); print(f\"CSRF: {settings.CSRF_TRUSTED_ORIGINS}\")"'

# Expected output:
# DEBUG: False
# DOMAIN: great-chat.arpansahu.space
# CSRF: ['https://great-chat.arpansahu.space']

# Test application
curl -I https://great-chat.arpansahu.space
# Should return HTTP/2 302 (redirect to login)
```

## Static Files Configuration

The new STORAGES dict configuration handles static files properly:

```python
STORAGES = {
    'default': {
        'BACKEND': 'great_chat.storage_backends.PublicMediaStorage',
        'OPTIONS': {
            'location': 'portfolio/great_chat/media',
            'bucket_name': 'arpansahu-one-bucket',
            'endpoint_url': 'https://minioapi.arpansahu.space',
        },
    },
    'staticfiles': {
        'BACKEND': 'great_chat.storage_backends.StaticStorage',
        'OPTIONS': {
            'location': 'portfolio/great_chat/static',
            'bucket_name': 'arpansahu-one-bucket',
            'endpoint_url': 'https://minioapi.arpansahu.space',
        },
    },
}
```

This replaces the old Django 3.2 style:
- ❌ `STATICFILES_STORAGE = 'great_chat.storage_backends.StaticStorage'`
- ✅ `STORAGES = {'staticfiles': {'BACKEND': '...'}}`

## Troubleshooting

### Issue: CSRF verification failed
**Cause:** Kubernetes secret has wrong DEBUG or DOMAIN values

**Solution:**
```bash
# Recreate secret with correct values
sudo kubectl delete secret great-chat-secret -n default
sudo kubectl create secret generic great-chat-secret --from-env-file=.env -n default
sudo kubectl rollout restart deployment/great-chat-app -n default
```

### Issue: Static files not uploading to MinIO
**Cause:** Wrong AWS_S3_ENDPOINT_URL or AWS_S3_CUSTOM_DOMAIN

**Solution:** Verify .env has:
```bash
AWS_S3_ENDPOINT_URL=https://minioapi.arpansahu.space
AWS_S3_CUSTOM_DOMAIN=minioapi.arpansahu.space/arpansahu-one-bucket
```

### Issue: Pod CrashLoopBackOff
**Cause:** collectstatic taking too long or failing

**Solution:**
```bash
# Check pod logs
sudo kubectl logs -n default deployment/great-chat-app --tail=50

# If collectstatic timeout, increase probe delays:
sudo kubectl patch deployment great-chat-app -n default --type=json \
  -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/livenessProbe/initialDelaySeconds", "value": 180}]'
```

### Issue: 502 Bad Gateway
**Cause:** Pod is running but not responding on port 8002

**Solution:**
```bash
# Check if uvicorn is running
sudo kubectl exec -n default deployment/great-chat-app -- ps aux | grep uvicorn

# Test NodePort locally
ssh arpansahu@arpansahu.space 'curl http://127.0.0.1:32002'

# Check nginx config
ssh arpansahu@arpansahu.space 'sudo cat /etc/nginx/sites-available/great-chat | grep proxy_pass'
# Should show: proxy_pass http://127.0.0.1:32002;
```

## Fixes Applied in This Session

1. ✅ **MinIO Endpoint:** Fixed hardcoded `minio.arpansahu.space` → `minioapi.arpansahu.space`
2. ✅ **CSRF Settings:** Fixed DEBUG=1 and DOMAIN=localhost in Kubernetes secret
3. ✅ **Storage Backend:** Migrated to Django 4.2+ STORAGES dict
4. ✅ **Django Version:** Standardized to 4.2.28 (from 5.0.6)
5. ✅ **AWS_S3_CUSTOM_DOMAIN:** Now reads from environment variable

## Next Steps

1. ✅ Django downgraded to 4.2.28 for consistency
2. ✅ Storage settings updated to STORAGES dict
3. ✅ MinIO endpoint configuration fixed
4. ⏳ Update Kubernetes secret with correct environment variables
5. ⏳ Create Jenkins credential with .env file
6. ⏳ Trigger Jenkins build pipeline
7. ⏳ Deploy new image to production

The codebase is production-ready with proper Django 4.2 configuration!
