
# Base image
FROM node:bookworm

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all other source files
COPY . .


CMD ["npm", "run", "dev"]
