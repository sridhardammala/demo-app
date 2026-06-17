# Official nginx image — extremely lightweight (~25MB).
# Think of this like using the AWS managed nginx AMI.
FROM nginx:alpine

# Remove the default nginx config and replace with ours.
# The default config doesn't have our /api/ proxy rule.
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy our HTML page into the directory nginx serves static files from.
# This is the equivalent of uploading files to an S3 bucket
# configured for static website hosting.
COPY index.html /usr/share/nginx/html/index.html

# nginx listens on port 80 by default.
# Again this is just documentation — port mapping happens in Kubernetes.
EXPOSE 80

# nginx starts automatically — no CMD needed.
# The base image already defines CMD ["nginx", "-g", "daemon off;"]