# Flask Postgres Nginx example

## Development
```
docker-compose up -d --build
```
```
docker-compose down -v
```

## Production
```
docker-compose -f docker-compose.prod.yaml up -d --build
```
```
docker-compose -f docker-compose.prod.yaml down -v
```

## Create database tables
```
docker-compose exec web bash
python
from app import *
with app.app_context():
    db.create_all()

exit()
exit
```

## Postgres Backups

Create backup folder:
```
docker-compose exec db bash -c "mkdir /var/lib/postgresql/data/backups"
```

Create backup:
```
docker-compose exec db bash -c "pg_dump --username=user --format=c database > /var/lib/postgresql/data/backups/backup_$(date +%Y-%m-%d).dump"
```

Restore backup:
```
docker-compose exec db bash -c "pg_restore -c --username=user -v -d database /var/lib/postgresql/data/backups/backup_2022-02-01.dump"
```

Copy backup:
```
docker cp db094c2d6cf9:/var/lib/postgresql/data/backups/backup_2022-02-01.dump /Users/dedol/backups
```
