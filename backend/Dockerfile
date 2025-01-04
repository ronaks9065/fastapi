# Success Dockerfile
FROM nginx:alpine

# Add a success message (optional)
RUN echo "Pipeline Success Test - Build Successful! RONAK" > /usr/share/nginx/html/index.html

# Expose the default HTTP port
EXPOSE 5000

CMD ["nginx", "-g", "daemon off;"]
