FROM node:18-alpine

# Create app directory
WORKDIR /usr/src/app

# Copy backend package manifest first for better caching
COPY SHL_GenAI_Project/backend/package*.json ./SHL_GenAI_Project/backend/

# Install only prod dependencies for smaller image
RUN npm --prefix SHL_GenAI_Project/backend install --production

# Copy the rest of the project
COPY . .

# Expose port
EXPOSE 8080

# Start the backend (Render will set PORT env)
CMD ["node", "SHL_GenAI_Project/backend/index.js"]
