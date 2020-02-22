FROM php:7.3.3-apache
# Install dependencies
RUN buildDeps=" \
        wget \
        git \
        ssh \
        less \
    "; \
    set -x \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Composer
RUN wget https://getcomposer.org/installer -O - -q | php -- --quiet && \
    mv composer.phar /usr/local/bin/composer
RUN docker-php-ext-install pdo pdo_mysql && docker-php-ext-enable pdo_mysql
EXPOSE 80
