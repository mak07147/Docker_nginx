FROM nginx
COPY . /etc/nginx/templates/nginx.conf.template
ENV NGINX_ENVSUBST_TEMPLATE_DIR=/etc/nginx/templates
ENV NGINX_ENVSUBST_OUTPUT_DIR=/etc/nginx
ENV NGINX_ENVSUBST_TEMPLATE_SUFFIX=.template
ENV ENV_TXT="Default text message from template"
EXPOSE 80
USER nginx
CMD ["nginx", "-g", "daemon off;"]
