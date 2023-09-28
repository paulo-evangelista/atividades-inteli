# ./server/Dockerfile

# Base image
FROM node:latest

RUN apt install -y python3

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

RUN npm install

# Copy all other source files
COPY . .

# Start the app
CMD ["npm", "run", "start:dev"]
