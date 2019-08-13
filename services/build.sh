VERSION=v0.0.1

docker build . -f api_gateway/Dockerfile -t api_gateway

docker tag api_gateway fouyer/api_gateway:$VERSION

docker push fouyer/api_gateway:$VERSION