## Example Server
Maven Spring project which currently loads a secure servlet backend with a REST controller and some hardcoded data. REACT JavaScript front_end is located src/main/web and creates a working GUI with some REST calls to show functionality
### Running Locally
Using bash enter the one of following commands
- `mvn package` This will build the project if you have not already.  
- `mvn spring-boot:run` This will deploy the project

### Back-End  
The Java back end has a client to call and API which lists drivers from the f1.  
A MySQL Database is integrated, which keeps an archive of the drivers and some information about them.  
Endpoints have been added to refresh and list the drivers in the database.  

### TODO!

Create a working and unique full stack packaged APP - affix a working react-redux front-end
- added multi-module pom Maven build
- setting up hello-world react-redux
