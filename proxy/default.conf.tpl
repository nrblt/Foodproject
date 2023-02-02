server {
    listen ${LISTEM_PORT};

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass   ${APP_HOST}:${APP_PORT};
        inlcude       /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}
