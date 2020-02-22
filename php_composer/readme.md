# Apache based PHP project layout with composer

Description:
	Composer dependency built into the php container image enables autoloader use,
	symfony component addition or various sundries.
	
Project implementation details:
	Two services are connected through the docker-compose.yml file.
	The "web" service (php7.3 + apache + composer) uses the ./php bind mount.
	
	The "db" service uses a named volume for data persistency.
	
## Usage:

```
docker-compose up -d 
```

