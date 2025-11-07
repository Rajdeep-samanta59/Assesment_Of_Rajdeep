FROM node:18-alpine

WORKDIR /usr/src/app

# Copy backend package manifest first for better caching
COPY SHL_GenAI_Project/backend/package*.json ./SHL_GenAI_Project/backend/

# Install only prod dependencies for smaller image
RUN npm --prefix SHL_GenAI_Project/backend install --production

# Copy the rest of the project
COPY . .

EXPOSE 8080

CMD ["node", "SHL_GenAI_Project/backend/index.js"]
