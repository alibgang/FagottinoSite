FROM nginx:latest 
RUN sleep 3
RUN mkdir -p /etc/systemd/system/
RUN mkdir -p /etc/nginx/sites-enabled
COPY gunicorn/ /etc/systemd/system/

# Test nginx
# RUN ln -s /etc/nginx/sites-available/fagottino /etc/nginx/sites-available    
RUN nginx -t
