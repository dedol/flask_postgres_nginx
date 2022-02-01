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

## Postgres Backups

Create backup folder:
```
docker-compose exec db bash -c "cd /var/lib/postgresql/data/ && mkdir backup"
```

Create backup:
```
docker-compose exec db bash -c "pg_dump --username=user --format=c database > /var/lib/postgresql/data/backup/backup_$(date +%Y-%m-%d).dump"
```

Restore backup:
```
docker-compose exec db bash -c "pg_restore -c --username=user -v -d database /var/lib/postgresql/data/backup/backup_2022-02-01.dump"
```
