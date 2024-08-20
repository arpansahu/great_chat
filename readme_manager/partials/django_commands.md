1. Test DB
  Django management command designed to test the basic functionality of the database. It performs a series of CRUD (Create, Read, Update, Delete) operations to ensure the database is working correctly.
```bash
python manage.py test_db
```

2. Test Cache
   Django management command designed to test the basic functionality of the caching system. It performs a set and get operation to ensure the cache is working correctly and validates the expiration of cache entries.
```bash
python manage.py test_cache
```

3. Test Channels
  Django management command designed to test the functionality of Django Channels, ensuring that it is properly configured and operational.
```bash
python manage.py test_channels
```

4. Sync Media to S3
  In case if you are using production database and debug mode is on. all the media send in the chats will be stored to local media folder which might not get synced to s3 bucket and when you run in production those media will be missing.
```bash
python manage.py sync_media_to_s3
```