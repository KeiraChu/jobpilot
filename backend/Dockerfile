FROM maven:3.9.9-eclipse-temurin-8 AS build
WORKDIR /workspace
ENV MAVEN_OPTS="-Xms128m -Xmx512m -XX:+UseSerialGC"
COPY pom.xml .
RUN mvn -B -DskipTests dependency:go-offline
COPY src ./src
RUN mvn -B package

FROM eclipse-temurin:8-jre
WORKDIR /app
COPY --from=build /workspace/target/Jobpilot-1.0-SNAPSHOT.jar app.jar
EXPOSE 8088
ENTRYPOINT ["java", "-jar", "app.jar"]
