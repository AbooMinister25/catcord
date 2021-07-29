# Pull node image
FROM node:14-alpine

# Run container in /app
WORKDIR /app

# Install dependencies
COPY package.json yarn.lock ./
RUN yarn set version berry
RUN echo "nodeLinker: node-modules" >> .yarnrc.yml
RUN yarn install

# Build for production
COPY . .
RUN yarn build

# Set NODE_ENV
ENV NODE_ENV production

# Expose port 3000
EXPOSE 3000

# Serve on node
CMD ["yarn", "start"]