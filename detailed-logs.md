### charliemeyer2000: 'start of documentation' @ 06/21/2023, 14:14:46 to assorted-scenthound-things

    Code Added:
        File: notes/scenter-app-learning.md
    + # Scenter App Learning
    + 
    + This is just notes and things i've learned/need to learn to undertstand and work with the SCENTER app. 
    + 
    + ## Summary
    + 
    + This application is used by scent-techs during their evaluation of dogs. It allows them to record information about the dog & the scent-check which will be saved and also sent to the dog parent. 
    + 
    + The Scenter App is a serverless application that uses AWS AppSync to communicate with a MySQL database. The application is written in TypeScript and uses the Serverless Framework to deploy the application to AWS. The Scenter App does not actually communicate with myTime, but it reads information from a replica. This replica also has some information from legacy systems before the migration to myTime (2022) and excludes sensitive information such as client information.
    + 
    + This all then is used in the frontend (a React app using TypeScript) to display information to the scent-techs and allow them to record information about the dog & scent-check.
    + 
    + ## Backend
    + 
    + 
    + ### Setup & Configuration
    + 
    + Before you start working with any of the code (even frontend code!) make sure that you have installed yarn (if you're used to `npm`, just run `npm install -g yarn` to install yarn globally). 
    + 
    + Also, reach out to Andy (or _insert manager here_) to get AWS credentials. This should be a `.csv` file that contains a key and a secret to create the credentials. First install the AWS CLI. 
    + 
    + 1. For MacOS users, download the pkg [here](https://awscli.amazonaws.com/AWSCLIV2.pkg), and then run the installer as you would any other application. If you want to install using the command line, follow instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). 
    + 1. For windows users, you can install it using the [AWS CLI MSI Installer (64 bit)](https://awscli.amazonaws.com/AWSCLIV2.msi) and follow the steps accordingly.
    + 1. For Linux, follow the `cURL` command and unzip it, and run the installer. 
    + 
    + Once you have the AWS CLI installed, run `aws configure` and enter the credentials from the `.csv` file. Ensure that you are creating a profile called "scenthound" (or whatever you want to call it, but this is what the `serverless.yml` file is looking for). To check that you have the correct credentials, you can run `aws s3 ls --profile scenthound` and it should list the buckets that are in the account, and you can verify that those are correct by logging in to the AWS website and checking the buckets.
    + 
    + 
    + ### `serverless.yml`
    + 
    + Of all the places to begin learning, think of this file as your _entry point_ into the application. This is a central configuration file that defines the infrastructure and deployment settings of the serverless application. Understanding what happens here - the configuration and all the things it communicates with & uses - is a way to understand the application as a whole.
    + 
    + * `serverless.yml` - `service`
    +     * this is the first line of the file, defining the name of the service (i.e. "scenter-backend"). 
    + * `serverless.yml` - `provider`
    +     * This specifies the cloud provider (i.e. AWS) and the runtime, profile, and region.
    + * `serverless.yml` - `environment`
    +     * Defines environment variables that are used throughout the application.
    + * `serverless.yml` - `httpApi`
    +     * Defines the http api that is used to communicate with the application. In this case, it just uses cors. 
    + * `serverless.yml` - `iam`
    +     * Defines the IAM roles that are used throughout the application and thier permissions for accessing AWS resources.
    + * `serverless.yml` - `custom`
    +     * Defines various custom settings that are used throughout the application.
    + * `serverless.yml` - `appSync`
    +     * This configures settings for AWS AppSync API. Specifically focusing on the schema - it defines the schema according to the `schemas/*.graphql` files. Furthermore, it establishes the dataSources of "lambdaSource" and "lambdaBatchSource" for the lambda functions. 
    +     * Finally, a majority of section is just defining resolvers for the various queries & mutations.
    + * `serverless.yml` - `functions`
    +     * This defines Lambda handles that are a part of the application. Crucially, _lambdaSource_ and _lambdaBatchSource_ are defined here.
    + 
    + #### `serverless.yml` - `custom`
    + 
    + As mentioned above, the **custom** section of the `serverless.yml` file defines various custom settings that are used throughout the application. Here's a walkthrough of the major sections within it:
    + 
    + * `serverless.yml` - `custom` - `defaults`
    +     * Defines a YML anchor to reuse common configuration settings & default values. 
    + * `serverless.yml` - `custom` - `dev` && `prod`
    +     * This section specifies configuration settings for the "dev" and "prod" stages. 
    + * `serverless.yml` - `custom` - `defaultSource` && `defaultBatchSource` 
    +     * These sections define YML anchors for the source configuration used in lambda functions. They set the data sources to "lambdaSource" and "batchLambdaSource", respectively.
    + 
    + ### `schemas/app.graphql`
    + 
    + (Assuming you've never used GraphQL before like me) - this is the file that contains the GraphQL schema definition for the application. At a high-level, GraphQL allows clients to request specific data and shape the response of the data. This is a way to reduce the amount of data that is sent back and forth between the client and the server. Before tackling all the things that are written, it's important to understand key components of the schema.
    + 
    + 1. Query - this is a way to get data from the server.
    + 2. Mutation - this is a way to change data on the server.
    + 3. Subscription - this is a way to get notified when data changes on the server.
    + 4. Scalar types - these are the primitive types that are used in the schema. 
    +     * String
    +     * Int
    +     * Float
    +     * Boolean
    +     * Long
    + 5. Interfaces - these are abstract types that define a set of fields that must be implemented by any object type that implements the interface (a la DSA1 for UVA students). 
    + 6. Types - types represent the object types in the schema. Each type has its own set of fields. 
    +     * Query Type - entry point for fetching data.
    +     * Mutation Type - operations that change data on the server.
    +     * Subscription Type - real time data streaming.
    +     * Others 
    + 7. Input Types - special types that are used to pass arguments to queries and mutations.
    + 8. Enums - special types that are used to define a set of constants.
    + 
    + #### `schemas/app.graphql` - Types
    + 
    + 1. `Query Type`
    + 
    + ```graphql
    + type Query {
    +   # Relay compatibility
    +   node(id: ID!): Node!
    +   appointment(id: ID, myTimeId: Long): Appointment
    +   status(id: ID, appointmentId: ID): AppointmentStatus!
    +   employee(id: ID!): Employee!
    +   location(id: ID, myTimeId: Int): Location!
    +   dog(id: ID, myTimeId: Int): Dog!
    +   client(id: ID!): Client!
    + 
    +   fieldOptions(fields: [String!]!): [FieldOptionsGroup!]!
    + 
    +   getAppointments(locationId: Int!, start: AWSDateTime, end: AWSDateTime): [Appointment!]!
    + 
    +   products: [Product!]!
    +   membershipTemplates(locationId: ID, myTimeId: Int): [MembershipTemplate!]!
    + }
    + ```
    + 
    + This is the entry point for fetching data. Notice the various required (marked by `!`) and optional fields. Also, since it implements the `Node` interface, it has a `node` field that can be used to fetch any object by its ID.
    + 
    + 2. `Mutation Type`
    + 
    + This represents the operations that can modify data. Note that the operations that acn modify data are all inputs. 
    + 
    + ```graphql
    + type Mutation {
    +   createStatus(data: CreateStatusInput!): AppointmentStatus!
    +   updateStatus(data: UpdateStatusInput!): AppointmentStatus!
    +   addAttachments(id: ID!, attachments: [AttachmentInput!]!): AppointmentStatus!
    +   removeAttachments(id: ID!, keys: [String!]!): AppointmentStatus!
    +   updateScentchecks(data: UpdateScentchecksInput!): AppointmentStatus!
    +   # timerStatus(id: ID!, status: TimerStatus): AppointmentStatus!
    +   pauseTimer(data: PauseTimerInput!): AppointmentStatus!
    +   startTimer(data: StartTimerInput!): AppointmentStatus!
    +   updateDog(data: UpdateDogInput!): Dog
    +   updateClient(data: UpdateClientInput!): Client
    +   markAppointment(data: MarkAppointmentInput!): Appointment
    + }
    + ```
    + 
    + These allow the basic _CRUD_ operations on the data.
    + 
    + 3. `Subscription Type`
    + 
    + This defines a subscription operation (similar to onSnapshot in Firebase, for Forge Interns) that can be used to 'subscribe' to real-time changes in data.
    + 
    + ```graphql
    + type Subscription {
    +   ## Arguments matched against return value of updateStatus mutation
    +   onUpdateStatus(id: ID!): AppointmentStatus
    +     @aws_subscribe(mutations: ["updateStatus"])
    + }
    + ```
    + 
    + #### `schemas/app.graphql` - Other
    + 
    + You can look around in the `app.graphql` file to see the various interfaces, types, inputs, and other declarations that are used in the schema. All of these will be used in the resolvers that are defined in the `serverless.yml` file.
    + 
    + ### Other
    + 
    + I would suggest looking around at other files within the backend, but the majority of what was written above is the most important. 
    + 
    + 
    + ## Frontend
    + 
    + ### Tools Used
    + 
    + Here's a basic rundown of the tools used (besides the obvious, like `create-react-app`).
    + 
    + 1. `react-router-dom` - used for routing within the application. You can see the main routing of the application in `src/Index.tsx`. 
    + 1. `react-redux` - 
    + 
    + ### Deployment
    + 
    + Currently (as of 6/20/23) the method of deployment is to simply run the following commands in the `scenter-app` directory:
    + 
    + 1. `yarn run build:prod` for production build or `yarn run build:dev` for development build.
    + 1. `bash deploy/upload.sh`
    + 
    + In the future pipelines should be made to automatically do this when pushing to dev/main, but this is what we do for now. 
    + 


    Code Removed:
        File: notes/scenter-app-learning.md



### charliemeyer2000: 'brian notes meeting 1' @ 06/20/2023, 22:13:59 to assorted-scenthound-things

    Code Added:
        File: .DS_Store

    File: notes/brian-notes.md
    + # Notes with Brian
    + 
    + ## Scenter App
    + 
    + Reading information from read-replica of the database rather than directly from the myTime database. So when you;re interacting with "myTime" data you're actually just interacting with replicas. 
    + 
    + Sensitive data is removed from the replicas, such as client information. There is also information mixed in from other legacy systems before migration about a year ago (2022).
    + 
    + ### Backend
    + 
    + AppSync is the aws technology that it uses. It is a toolkit for building GraphQL api's. There is a YML file that configures the backend `serverless.yml`. This includes appsync and lambda functions, and is largely declarative (with some exceptions for different environments, _prod_, _dev_, etc). This only uses **2** different _resolvers_.  The datasource, called "lambdasource" is the resolver, and there's another one called "batchLambdaSource." These are two lambda resolvers for everything. This is not standard (you're supposed to use VTL) but it's a workaround for the fact that the data is coming from a read-replica.
    + 
    + #### GraphQl
    + 
    + * This is a query language that gets exactly what you want (objects, fields, etc) that you've requested to save back-and-forth wasted data.
    +     * Scales costs relatively to what you need, in addition to caching and bashing. 
    + * check this out at `app.graphql` to see the types and queries that are available.
    + * the configuration file `serverles.yml` communicates with the graphql schema to create the api.
    + 
    + 
    + ```graphql
    + query GetLocation {
    +     location(myTimeId: 12345) {
    +         name
    +         companyId
    + 
    +         scentchecks {
    +             dog {
    +                 name
    + 
    +                 client {
    +                     firstName
    +                 }
    +             }
    + 
    +         }
    +     }
    + }
    + 
    + ```
    + 
    + #### Default Batch Source (Resolver)
    + 
    + `handlers.ts` is the file that returns the same things as a single resolver except it does it in batches through the `AppSyncResolverHandler`. All mysql queries are made in terms of batches. 
    + 
    + 
    + #### Data Sources
    + 
    + * `db`: dynamodb - mySql, where we get all of our data from MyTime and _some_ of our application data (i.e. scentchecks). 
    + * `mysql`: myTime 
    + 
    + #### Mutations
    + 
    + How you make things change. `handlemutation` is handled by the simple resolver instead of the batch resolver. 
    + 
    + 
    + #### Subscriptions
    + 
    + 
    + 
    + ### Summary
    + 
    + AppSync exposes an api through the `serverless.yml` file which is read through the `app.graphql` file. Those resolvers can be handled differently depending on specific needs. 
    + 
    + 
    + ### Fragments
    + 
    + Fragments are a way to reuse queries. 
    + 
    + ```graphql
    + 
    + 


    Code Removed:
        File: .DS_Store

    File: notes/brian-notes.md



### charliemeyer2000: 'added a period.' @ 06/19/2023, 13:17:39 to website

    Code Added:
        File: index.html
    + <p>Hi! I'm Charlie Meyer, an programmer/developer from Washington, D.C., currently completing undergraduate studies in computer science at UVA. I'm into weightlifting, skateboarding, embroidery, an occasional set of SSBM and also like movie making. I'm also working on a startup with a buddy of mine called HymnAI, it's pretty sweet and I'm super proud of it.</p>


    Code Removed:
        File: index.html
    - <p>Hi! I'm Charlie Meyer, an programmer/developer from Washington, D.C., currently completing undergraduate studies in computer science at UVA. I'm into weightlifting, skateboarding, embroidery, an occasional set of SSBM and also like movie making  I'm also working on a startup with a buddy of mine called HymnAI, it's pretty sweet and I'm super proud of it.</p>



### charliemeyer2000: 'added more to scrolling svg' @ 06/19/2023, 13:15:49 to charliemeyer2000

    Code Added:
        File: README.md
    +     <a href="https://github.com/charliemeyer2000"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=FFDEAD&center=true&vCenter=true&width=435&lines=Full-stack+developer;kubectl apply -f ingress.yml;Professional Proompter;Late-night+coffee+drinker;$\forall_x \in \mathbb{N}$;:wq;int getRandomNumber(){return 4};display:grid place-content:center;ngrok http 9000" alt="Typing SVG of various programmer humor jokes and other things about me" /></a>


    Code Removed:
        File: README.md
    -     <a href="https://github.com/charliemeyer2000"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=FFDEAD&center=true&vCenter=true&width=435&lines=Full-stack+developer;kubectl apply -f ingress.yml;Professional Proompter;Late-night+coffee+drinker;$\forall_x \in \mathbb{N}$;:wq;int getRandomNumber(){return 4};display:grid place-content:center" alt="Typing SVG of various programmer humor jokes and other things about me" /></a>



### charliemeyer2000: 'changed writeup' @ 06/17/2023, 19:01:20 to charliemeyer2000

    Code Added:
        File: README.md
    +  Welcome to my GitHub! I'm Charlie Meyer, a full-time student at UVA who also loves to code things - full-stack applications, and ml models, and much more. I personally believe GitHub and personal websites are much better than LinkedIn to show off who you are & what you're passionate about. I have a LinkedIn, but I'd prefer you look here instead! There are tons of incredibly helpful resources including resources I've used throughout my coding journey, so check them out. Check out my website <a href="https://charliemeyer.xyz" target="_blank" rel="noopener noreferrer" style="color: #FFD700;">charliemeyer.xyz</a> and the startup i'm working on <a href="https://hymn.market" target="_blank" rel="noopener noreferrer" style="color: #FFD700;"> hymn.market </a> and email <a href="mailto:charlie@charliemeyer.xyz" style="color: #FFD700; " target="_blank" rel="noopener noreferrer">charlie@charliemeyer.xyz</a>  for any inquiries.


    Code Removed:
        File: README.md
    -  Welcome to my GitHub! I'm Charlie Meyer, a full-time student at UVA who also loves to code things - websites, projects, and ml models. The goal of my GitHub is to be a place to display my projects and also be a space for new developers to find useful resources to get started. I personally believe GitHub and personal websites are much better than LinkedIn to show off who you are & what you're passionate about. I have a LinkedIn, but I'd prefer you look here instead! Check out my website <a href="https://charliemeyer.xyz" target="_blank" rel="noopener noreferrer" style="color: #FFD700;">charliemeyer.xyz</a> and the startup i'm working on <a href="https://hymn.market" target="_blank" rel="noopener noreferrer" style="color: #FFD700;"> hymn.market </a> and email <a href="mailto:charlie@charliemeyer.xyz" style="color: #FFD700; " target="_blank" rel="noopener noreferrer">charlie@charliemeyer.xyz</a>  for any inquiries.



### charliemeyer2000: 'added hymn.market' @ 06/17/2023, 18:54:24 to charliemeyer2000

    Code Added:
        File: README.md
    +  Welcome to my GitHub! I'm Charlie Meyer, a full-time student at UVA who also loves to code things - websites, projects, and ml models. The goal of my GitHub is to be a place to display my projects and also be a space for new developers to find useful resources to get started. I personally believe GitHub and personal websites are much better than LinkedIn to show off who you are & what you're passionate about. I have a LinkedIn, but I'd prefer you look here instead! Check out my website <a href="https://charliemeyer.xyz" target="_blank" rel="noopener noreferrer" style="color: #FFD700;">charliemeyer.xyz</a> and the startup i'm working on <a href="https://hymn.market" target="_blank" rel="noopener noreferrer" style="color: #FFD700;"> hymn.market </a> and email <a href="mailto:charlie@charliemeyer.xyz" style="color: #FFD700; " target="_blank" rel="noopener noreferrer">charlie@charliemeyer.xyz</a>  for any inquiries.


    Code Removed:
        File: README.md
    -  Welcome to my GitHub! I'm Charlie Meyer, a full-time student at UVA who also loves to code things - websites, projects, and ml models. The goal of my GitHub is to be a place to display my projects and also be a space for new developers to find useful resources to get started. I personally believe GitHub and personal websites are much better than LinkedIn to show off who you are & what you're passionate about. I have a LinkedIn, but I'd prefer you look here instead! Check out my website <a href="https://charliemeyer.xyz" target="_blank" rel="noopener noreferrer" style="color: #FFD700;">charliemeyer.xyz</a> and email <a href="mailto:charlie@charliemeyer.xyz" style="color: #FFD700; " target="_blank" rel="noopener noreferrer">charlie@charliemeyer.xyz</a>  for any inquiries.



### charliemeyer2000: 'added kuberenetes' @ 06/17/2023, 14:58:24 to charliemeyer2000

    Code Added:
        File: README.md
    +                 <li style="display:inline"><a href="https://kubernetes.io/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Kuberenetes</a></li>


    Code Removed:
        File: README.md



### charliemeyer2000: 'added github' @ 06/17/2023, 14:56:27 to charliemeyer2000

    Code Added:
        File: README.md
    +                 <li style="display:inline"><a href="https://github.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">GitHub</a></li>


    Code Removed:
        File: README.md



### charliemeyer2000: 'added fav fullstack tools' @ 06/17/2023, 14:48:29 to charliemeyer2000

    Code Added:
        File: README.md
    +         <li><h2 style="color: #FFDEAD">My Fav Fullstack Tools</h2>
    +             <ul>
    +                 <li style="display:inline"><a href="https://react.dev/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">React</a></li>
    +                 <li style="display:inline"><a href="https://redux.js.org/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Redux</a></li>
    +                 <li style="display:inline"><a href="https://nextjs.org/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Nextjs</a></li>
    +                 <li style="display:inline"><a href="https://github.com/css-modules/css-modules"style="color: #FFD700"target="_blank" rel="noopener noreferrer">CSS Modules</a></li>
    +                 <li style="display:inline"><a href="https://www.docker.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Docker</a></li>
    +                 <li style="display:inline"><a href="https://www.nginx.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Nginx</a></li>
    +                 <li style="display:inline"><a href="https://www.mongodb.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">MongoDB</a></li>
    +                 <li style="display:inline"><a href="https://firebase.google.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Firebase</a></li>
    +                 <li style="display:inline"><a href="https://cloud.google.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Google Cloud</a></li>
    +                 <li style="display:inline"><a href="https://vercel.com/"style="color: #FFD700"target="_blank" rel="noopener noreferrer">Vercel</a></li>
    +             </ul>


    Code Removed:
        File: README.md



### charliemeyer2000: 'added another tool' @ 06/17/2023, 13:54:46 to charliemeyer2000

    Code Added:
        File: README.md
    +     <p align="center"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer">  </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> </a> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> </a> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> </a>  <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a><a href="https://www.typescriptlang.org/" target="_blank" rel="noopener noreferer"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-plain.svg" alt="typescript" width="40" height="40" /></a><a href="https://python.langchain.com/docs/get_started/introduction.html" target="_blank" rel="noopener noreferer"><img src="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22></text></svg>" alt="langchain" width="40" height="40" /></a><a href="https://pypi.org/project/chromadb/" target="_blank" rel="noopener noreferer"><img src="https://docs.trychroma.com/img/chroma.png" alt="chromadb"  height="40" /></a></p>


    Code Removed:
        File: README.md
    -     <p align="center"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer">  </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> </a> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> </a> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> </a>  <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a><a href="https://www.typescriptlang.org/" target="_blank" rel="noopener noreferer"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-plain.svg" alt="typescript" width="40" height="40" /></a><a href="https://python.langchain.com/docs/get_started/introduction.html" target="_blank" rel="noopener noreferer"><img src="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22></text></svg>" alt="langchain" width="40" height="40" /></a></p>




