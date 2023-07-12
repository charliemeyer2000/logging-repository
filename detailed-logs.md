### charliemeyer2000: 'resources 4 recommendation system & web app notes' @ 07/12/2023, 17:40:29 to assorted-scenthound-things

    Code Added:
        File: notes/list-of-resources.md
    + # List of Resources
    + 
    + List of resources for documentation on dogs for building the reccomendation system/LLM.
    + 
    + ## Scenthound
    + 
    + 1. [Breed Book](https://learnerresources.s3.eu-west-1.amazonaws.com/113354/learner_resource_uploads/ad0a80619bee20bca42f595a21/Breed%20Book%202.2.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQZVLRHER6MLZQEAI%2F20230712%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20230712T205749Z&X-Amz-Expires=30&X-Amz-SignedHeaders=host&X-Amz-Signature=3fd7bbbfdb504d69f450b391a11909e8f5472819cd6e2a5e54aea23929f44bfd)
    +     - This contains both breed information and information for suggestions for pet products based on the breed.
    +     - This will be SUPER important to create houndswell recommendations. This could almost be done by hand, but it would be a lot of work. 
    + 1. Scenthound Database(s) **ask manaar to send csv's to me**
    +     - Gather a list of Scentchecks & purhcase history based on that scentcheck (if data is good enough, it's possible to train a model to predict a product based on the scentcheck, or just use the scentcheck to narrow down the list of products to suggest with sklearn)
    +     - Get purchase history, scentcheck data, feature details
    +     - other relevant/helpful information
    + 1. Others?
    + 
    + ## From Jim
    + 
    + I have a very stream-of-consciousness from the meeting with him, this is just a super succinct and heavily compacted version of it. Also, much of what Jim mentioned was also provided by Dr. Krane, so I've avoided repeating information.
    + 
    + 1. AKC Website (if permissible)
    + 1. Veterinary Schools, specifically VT
    + 1. Other european/international kennel clubs, which the AKC may have data from
    +     - 
    + 1. Books:
    +     - "The Complete Dog Book", AKC (i can't find a pdf online)
    +         * i found this [super old version](https://ia800308.us.archive.org/13/items/completebookofdo00leig/completebookofdo00leig.pdf) though? 
    +     - ["Tips for Responsible Dog Owners"](http://images.akc.org/pdf/ebook/Responsible_Dog_Owners.pdf)
    + 1. - [Evolutionary Anthropology](https://evolutionaryanthropology.duke.edu/research/dogs)
    + 
    + ## From Dr. Krane
    + 
    + 1. [Veternary Partner](https://veterinarypartner.vin.com/default.aspx?pid=19239&id=)
    +     - Contains information on diseases/conditions, care, toxicities and behavior of dogs. 
    + 1. [Pet Place](https://www.petplace.com/)
    +     - More of an article-based, consumer-friendly site. Definitely more "our speed," as its more general recommendations.
    + 1. [Plumb's](https://plumbs.com/)
    +     - Veterinary drug handbook. Contains information on drugs, dosages, etc.
    +     - They have a free trial but also a subscription service, as well. This contains pretty specific information about drugs and dosages. Some of the information may be a little too specific for our purposes, but it couldn't hurt to have our model be as accurate as possible.
    +     - Look into their open-sourced data, as well:
    +         * [Plumb's Veterinary Drug Handbook](resources/Plumb-s-Veterinary-Drug-Handbook-Sixth-Edition_2.pdf)
    + 1. [AAHA](https://www.aaha.org/)
    +     - American Animal Hospital Association
    +     - Contains information on veterinary care, etc.
    +     - Also pretty scientific, but look into open source resources they offer (there's a lot of them on their site to look through):
    +         * [AAHA Dental Guidelines](https://www.aaha.org/globalassets/02-guidelines/dental/aaha_dental_guidelines.pdf)
    +         * [AAHA Nutrition and Weight Management](https://www.aaha.org/globalassets/02-guidelines/2021-nutrition-and-weight-management/resourcepdfs/new-2021-aaha-nutrition-and-weight-management-guidelines-with-ref.pdf)
    +         * [AAHA Behavior Management Guidelines](https://www.aaha.org/globalassets/02-guidelines/behavior-management/2015_aaha_canine_and_feline_behavior_management_guidelines_final.pdf)
    + 1. [ACVS](https://www.acvs.org/)
    +     - QUite specific documentation on various surgical procedures, etc. If you search by "canine" you can find some dog-specific articles about various procedures, such as [hip dysplasia](https://www.acvs.org/small-animal/canine-hip-dysplasia/), etc.
    + 1. [ACVN](https://acvn.org/)
    +     - MOstly a certification board, couldn't find much information from their site. 
    +     - [FAQ](https://acvn.org/frequently-asked-questions/) has some helpful tidbits
    + 1. [Whole Dog Journal](https://www.whole-dog-journal.com/)
    +     - Dog journal/magazine, contains information that would be helpful for consumers (not too specific, not too general). 
    +     - Contains info on dog food, behavior, training, health, care, and lifestyle.
    +     - Will be a pain in the *** to scrape, but is incredibly good for what we're looking for. 
    + 1. [OFA](https://ofa.org/chic-programs/)
    +     - Contains some odd infomration about various dog screenings, etc. From what i've seen, the csv's and pdf's aren't very helpful at all.
    + 1. [AVMA](https://www.avma.org/)
    +     - Not super helpful except for [this database of studies](https://ebusiness.avma.org/aahsd/study_search.aspx). If we wanted to, we could scrape this against a list of common dog diseases/conditions and see if we can find any studies that would be helpful for our model.
    + 1. [ASPCA](https://www.aspca.org/)
    +     - Contains information on animal poison control, animal cruelty, etc. 
    +     - Has a section on dogs with information like:
    +         * [General Dog Care](https://www.aspca.org/pet-care/dog-care/general-dog-care)
    +         * [Diy Canine Enrichment](https://www.aspca.org/pet-care/dog-care/canine-diy-enrichment)
    +         * 5-6 more articles that are pretty general and consumer-friendly
    + 
    + 

    File: notes/resources/Plumb-s-Veterinary-Drug-Handbook-Sixth-Edition_2.pdf

    File: notes/web-app.md


    Code Removed:
        File: notes/list-of-resources.md

    File: notes/resources/Plumb-s-Veterinary-Drug-Handbook-Sixth-Edition_2.pdf

    File: notes/web-app.md
    - ### Hello-bar



### charliemeyer2000: 'web app thing' @ 07/10/2023, 16:40:22 to assorted-scenthound-things

    Code Added:
        File: notes/meeting-with-jim.md
    + ## Other sites
    + 
    + - [Evolutionary Anthropology](https://evolutionaryanthropology.duke.edu/research/dogs)
    + 
    + 
    + 

    File: notes/web-app.md
    + # Web App
    + 
    + Talks about trial bookings, filling out a Zoho form (collecting lead information) which goes to Zoho CRM. They then go to the web app, fill out a form, and then books in myTime. 
    + 
    + Effectively all determined by url parameters. 
    + 
    + Collects payment information. Doesn't add membership to client, it sends an email to the scenter and the scenter adds it manually. 
    + 
    + ## Founding Memberships, Trial booking, Referrals
    + 
    + ### Referrals
    + 
    + Referral link that goes to a landing page that goes to the web app that inputs 
    + 
    + 
    + ### What we want to do
    + 
    + Trial booking rollout to 5 other locations. We want to add:
    + 
    + 1. Adding a modal to the end of the process to remind them to bring vaccination proof.
    +     * Double reminder to bring vaccination proof (see photo of what petco does).
    + 1. Founding memberships - send an eamil to the scenter inbox, saying "this member 
    + 1. Client label in myTime
    + 
    + ### Priority
    + 
    + 1. CRM Field
    + 1. Modal
    + 1. Email notifying scenter inbox of a new trial booking
    +     * works on founding memebrship, needs to work on trial booking
    + 1. MyTime Label
    +     * needs to work on trial booking
    + 
    + 
    + ### Login Information
    + 
    + * Zoho check chats with Freddy and Meiling
    +     * If we don't have permissions let Andy know.
    + * Reach out to Brian to have him quickly go over web app codebase. 
    + 
    + 
    + ### Priority against Scenter App
    + 
    + * Focus on web app this week, re-evaluate at the end of this week. 
    + 
    + 
    + ### COnfluence Space
    + 
    + "Operation document" - contains:
    + 
    + * SCENTHOUND-OS space -> operation document -> recodrded videos about the web app. 
    + 
    + 
    + ### Hello-bar
    + 


    Code Removed:
        File: notes/meeting-with-jim.md

    File: notes/web-app.md



### charliemeyer2000: 'added more tools & languages' @ 07/07/2023, 15:05:56 to charliemeyer2000

    Code Added:
        File: README.md
    +     <p align="center"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer">  </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> </a> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> </a> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> </a>  <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a><a href="https://www.typescriptlang.org/" target="_blank" rel="noopener noreferer"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-plain.svg" alt="typescript" width="40" height="40" /></a><a href="https://python.langchain.com/docs/get_started/introduction.html" target="_blank" rel="noopener noreferer"><img src="https://em-content.zobj.net/thumbs/160/apple/155/parrot_1f99c.png" alt="langchain" width="40" height="40" /></a><a href="https://pypi.org/project/chromadb/" target="_blank" rel="noopener noreferer"><img src="https://docs.trychroma.com/img/chroma.png" alt="chromadb"  height="40" /></a><a href="https://www.pinecone.io/" target="_blank" rel="noopener noreferer"><img src="https://seeklogo.com/images/P/pinecone-icon-logo-AF8B5B7F96-seeklogo.com.png" alt="pinecone"  height="40" /></a><a href="https://www.postgresql.org/" target="_blank" rel="noopener noreferer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/1200px-Postgresql_elephant.svg.png" alt="postgres"  height="40" /></a></p>


    Code Removed:
        File: README.md
    -     <p align="center"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer">  </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> </a> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> </a> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> </a>  <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a><a href="https://www.typescriptlang.org/" target="_blank" rel="noopener noreferer"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-plain.svg" alt="typescript" width="40" height="40" /></a><a href="https://python.langchain.com/docs/get_started/introduction.html" target="_blank" rel="noopener noreferer"><img src="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22></text></svg>" alt="langchain" width="40" height="40" /></a><a href="https://pypi.org/project/chromadb/" target="_blank" rel="noopener noreferer"><img src="https://docs.trychroma.com/img/chroma.png" alt="chromadb"  height="40" /></a></p>



### charliemeyer2000: 'meeting w/jim about data sources' @ 07/07/2023, 12:42:50 to assorted-scenthound-things

    Code Added:
        File: .gitignore
    + suggestions_reformatting/.DS_Store
    + 

    File: notes/meeting-with-jim.md
    + # Meeting w/Jim & Andy
    + 
    + humane society of the united states (mixed/rescue dog type stuff). Not as friendly to data, but not as restrictive (copyright, etc). 
    + 
    + AKC comes up with breed standard... so that's kind of weird why you can't copyright the information. 
    + 
    + ## Breed Organizations (other)
    + 
    + European orgs - 
    + * AKC stolen from German Kennel Society? 
    +     * Have multiple kennel club(s)
    + * AKC data repackaged into somewhere else?
    + 
    + ## Scenthound DNA
    + 
    + * Breed-specific DNA stuff with size, etc. (purebreds only)
    + 
    + ## Books
    + 
    + "Dogs" - colored, pretty. has height, average weight, etc. 
    + 
    + ## Veterans Schools (VT, etc)
    + 
    + * Veterinary schools w/professors that have a study area of something genetic-related in dogs. 
    + * VT Prof - rare colors & breeds of animals, including dogs. 
    + * SOmeone dooming research in genetic testing in dogs, find a prof that is a data list of things that a breed carries. 
    + * American College of Veterinary Dermatology, Dentistry
    + 
    + ## OFA - Orthopedic Foundation for Animals
    + 
    + hips, elbows, etc.
    + Also has CAER
    + American college of veterinary ophthalmologists
    + 
    + ## Penn Hip
    + 
    + * Hip dysplasia
    + 
    + ## Big Journals
    + 
    + * Journal of the American Veterinary Medical Association
    + * AVMA.org - American Veterinary Medical Association
    + * Veterinary Information Network
    +     * more medical stuff (not breed-specific)
    +     * we probably won't have any access to it since we're not vets. 
    + * American Journal of Veterinary Research
    +     * Animal health studies database. 
    +     * get a contact (?)
    + 
    + ## Witness, Embark, etc
    + 
    + DNA companies that have data. Companies may be willing to share DNA-based data. 
    + 
    + ## Published Books
    + 
    + * "How to select a puppy" - by the American Kennel Club
    + * "how to select a purebred for me"
    + * "the complete dog book" - akc
    + 
    + ## Big words
    + 
    + - atopy - allergies
    + 
    + 
    + 

    File: suggestions_reformatting/.DS_Store


    Code Removed:
        File: .gitignore

    File: notes/meeting-with-jim.md

    File: suggestions_reformatting/.DS_Store



### charliemeyer2000: 'stuff' @ 07/05/2023, 13:15:40 to assorted-scenthound-things

    Code Added:
        File: .gitignore
    + suggestions_reformatting/shortcuts.csv
    + suggestions_reformatting/output.ts
    + suggestions_reformatting/suggestions.ts


    Code Removed:
        File: .gitignore



### charliemeyer2000: 'quick web speech demo' @ 06/28/2023, 15:18:49 to assorted-scenthound-things

    Code Added:
        File: .gitignore
    + 
    + # ignore node_modules and other things within nextjs app called "tts-demo"
    + tts-demo/node_modules
    + tts-demo/.next
    + tts-demo/package-lock.json
    + 

    File: tts-demo/.gitignore
    + # See https://help.github.com/articles/ignoring-files/ for more about ignoring files.
    + 
    + # dependencies
    + /node_modules
    + /.pnp
    + .pnp.js
    + 
    + # testing
    + /coverage
    + 
    + # next.js
    + /.next/
    + /out/
    + 
    + # production
    + /build
    + 
    + # misc
    + .DS_Store
    + *.pem
    + 
    + # debug
    + npm-debug.log*
    + yarn-debug.log*
    + yarn-error.log*
    + 
    + # local env files
    + .env*.local
    + 
    + # vercel
    + .vercel
    + 
    + # typescript
    + *.tsbuildinfo
    + next-env.d.ts

    File: tts-demo/README.md
    + This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).
    + 
    + ## Getting Started
    + 
    + First, run the development server:
    + 
    + ```bash
    + npm run dev
    + # or
    + yarn dev
    + # or
    + pnpm dev
    + ```
    + 
    + Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
    + 
    + You can start editing the page by modifying `pages/index.js`. The page auto-updates as you edit the file.
    + 
    + [API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.js`.
    + 
    + The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.
    + 
    + This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.
    + 
    + ## Learn More
    + 
    + To learn more about Next.js, take a look at the following resources:
    + 
    + - [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
    + - [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
    + 
    + You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!
    + 
    + ## Deploy on Vercel
    + 
    + The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.
    + 
    + Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

    File: tts-demo/assets/mic.svg
    + <?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->
    + <svg fill="#000000" width="800px" height="800px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg">
    +     <path d="M15.965 22h0.238c2.78 0 4.797-2.050 4.797-4.874v-11.919c0-2.92-2.108-5.207-4.798-5.207h-0.237c-2.738 0-4.965 2.336-4.965 5.207v11.919c0 2.779 2.135 4.874 4.965 4.874zM13 5.207c0-1.768 1.33-3.207 2.965-3.207h0.238c1.595 0 2.797 1.379 2.797 3.207v11.919c0 1.718-1.124 2.874-2.798 2.874h-0.237c-1.746 0-2.965-1.181-2.965-2.874zM25 11c-0.552 0-1 0.448-1 1v4.159c0 5.95-2.124 8.842-6.492 8.842h-2.973c-5.713 0-6.535-4.808-6.535-8.841v-4.159c0-0.552-0.448-1-1-1s-1 0.448-1 1v4.159c0 6.89 2.872 10.841 8.535 10.841h0.465v3h-5c-0.552 0-1 0.448-1 1s0.448 1 1 1h12c0.552 0 1-0.448 1-1s-0.448-1-1-1h-5v-3h0.508c3.874 0 8.492-1.881 8.492-10.842v-4.159c0-0.552-0.448-1-1-1z"></path>
    + </svg>

    File: tts-demo/jsconfig.json
    + {
    +   "compilerOptions": {
    +     "paths": {
    +       "@/*": ["./*"]
    +     }
    +   }
    + }

    File: tts-demo/modals/ErrorPopup.js
    + import styles from "@/styles/ErrorPopup.module.css";
    + 
    + export default function ErrorPopup({ message, onClose }) {
    +   return (
    +     <div className={styles.container}>
    +       <div className={styles.content}>
    +         <p>{message}</p>
    +         <button onClick={onClose}>Close</button>
    +       </div>
    +     </div>
    +   );
    + }

    File: tts-demo/next.config.js
    + /** @type {import('next').NextConfig} */
    + const nextConfig = {
    +   reactStrictMode: true,
    + }
    + 
    + module.exports = nextConfig

    File: tts-demo/package.json
    + {
    +   "name": "tts-demo",
    +   "version": "0.1.0",
    +   "private": true,
    +   "scripts": {
    +     "dev": "next dev",
    +     "build": "next build",
    +     "start": "next start",
    +     "lint": "next lint"
    +   },
    +   "dependencies": {
    +     "next": "13.4.7",
    +     "react": "18.2.0",
    +     "react-dom": "18.2.0"
    +   }
    + }

    File: tts-demo/pages/_app.js
    + import '@/styles/globals.css'
    + 
    + export default function App({ Component, pageProps }) {
    +   return <Component {...pageProps} />
    + }

    File: tts-demo/pages/_document.js
    + import { Html, Head, Main, NextScript } from 'next/document'
    + 
    + export default function Document() {
    +   return (
    +     <Html lang="en">
    +       <Head />
    +       <body>
    +         <Main />
    +         <NextScript />
    +       </body>
    +     </Html>
    +   )
    + }

    File: tts-demo/pages/api/hello.js
    + // Next.js API route support: https://nextjs.org/docs/api-routes/introduction
    + 
    + export default function handler(req, res) {
    +   res.status(200).json({ name: 'John Doe' })
    + }

    File: tts-demo/pages/index.js
    + import Head from "next/head";
    + import { Inter, Miriam_Libre } from "next/font/google";
    + import styles from "@/styles/Home.module.css";
    + import { useEffect, useState } from "react";
    + import ErrorPopup from "@/modals/ErrorPopup";
    + import microphone from "@/assets/mic.svg";
    + import Image from "next/image";
    + 
    + const inter = Inter({ subsets: ["latin"] });
    + 
    + export default function Home() {
    +   const [error, setError] = useState(false);
    +   const [recognition, setRecognition] = useState(null);
    +   const [isListening, setIsListening] = useState(false);
    +   const [finalTranscript, setFinalTranscript] = useState("");
    +   const [interimTranscript, setInterimTranscript] = useState("");
    + 
    +   useEffect(() => {
    +     if (!("webkitSpeechRecognition" in window)) {
    +       setError(true);
    +     } else {
    +       setError(false);
    +       setRecognition(new window.webkitSpeechRecognition());
    +     }
    +   }, []);
    + 
    +   useEffect(() => {
    +     if (recognition) {
    +       recognition.continuous = true;
    +       recognition.interimResults = true;
    + 
    +       recognition.onstart = () => {
    +         setIsListening(true);
    +       };
    + 
    +       recognition.onerror = (event) => {
    +         // Handle error
    +       };
    + 
    +       recognition.onend = () => {
    +         setIsListening(false);
    +       };
    + 
    +       recognition.onresult = (event) => {
    +         let final = "";
    +         let interim = "";
    +         for (let i = event.resultIndex; i < event.results.length; ++i) {
    +           if (event.results[i].isFinal) {
    +             final += event.results[i][0].transcript;
    +           } else {
    +             interim += event.results[i][0].transcript;
    +           }
    +         }
    +         setFinalTranscript((prevState) => prevState + " " + final);
    +         setInterimTranscript(interim);
    +       };
    +     }
    +   }, [recognition]);
    + 
    +   const handleRecognition = () => {
    +     if (recognition) {
    +       if (isListening) {
    +         recognition.stop();
    +       } else {
    +         // setFinalTranscript("");
    +         setInterimTranscript("");
    +         recognition.lang = "en-US";
    +         recognition.start();
    +       }
    +     }
    +   };
    + 
    +   const handleCloseError = () => {
    +     setError(false);
    +   };
    + 
    +   return (
    +     <>
    +       <Head>
    +         <title>Web Speech Demo</title>
    +         <link
    +           rel="icon"
    +           href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22></text></svg>"
    +         />
    +       </Head>
    +       <main className={`${styles.main} ${inter.className}`}>
    +         <div className={styles.textHeader}>
    +           <h1 className={styles.title}>Web Speech Demo</h1>
    +           <p className={styles.description}>
    +             This is a quick demo of the Web Speech API. I think this should work
    +             well for the SCENTER app. I think that we could also make a quick
    +             custom rich text editor so that scent techs can also edit notes &
    +             other stuff and have it look pretty, but for the beta version that's
    +             not really necessary, but I think in the meantime just using the
    +             text box we have is good enough.
    +           </p>
    +         </div>
    + 
    +         <div className={styles.container}>
    +           <div
    +             className={`${styles.imageContainer} ${
    +               isListening && styles.active
    +             }`}
    +           >
    +             <Image
    +               src={microphone}
    +               className={`${styles.microphone}`}
    +               alt="microphone"
    +               onClick={handleRecognition}
    +             />
    +           </div>
    +           <p className={styles.text}>{finalTranscript}</p>
    +           <p className={styles.iterim}>{interimTranscript}</p>
    +         </div>
    +         {error && (
    +           <ErrorPopup
    +             message="There was an error loading the Speech Recognition API."
    +             onClose={handleCloseError}
    +           />
    +         )}
    +       </main>
    +     </>
    +   );
    + }

    File: tts-demo/public/favicon.ico

    File: tts-demo/public/next.svg
    + <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 394 80"><path fill="#000" d="M262 0h68.5v12.7h-27.2v66.6h-13.6V12.7H262V0ZM149 0v12.7H94v20.4h44.3v12.6H94v21h55v12.6H80.5V0h68.7zm34.3 0h-17.8l63.8 79.4h17.9l-32-39.7 32-39.6h-17.9l-23 28.6-23-28.6zm18.3 56.7-9-11-27.1 33.7h17.8l18.3-22.7z"/><path fill="#000" d="M81 79.3 17 0H0v79.3h13.6V17l50.2 62.3H81Zm252.6-.4c-1 0-1.8-.4-2.5-1s-1.1-1.6-1.1-2.6.3-1.8 1-2.5 1.6-1 2.6-1 1.8.3 2.5 1a3.4 3.4 0 0 1 .6 4.3 3.7 3.7 0 0 1-3 1.8zm23.2-33.5h6v23.3c0 2.1-.4 4-1.3 5.5a9.1 9.1 0 0 1-3.8 3.5c-1.6.8-3.5 1.3-5.7 1.3-2 0-3.7-.4-5.3-1s-2.8-1.8-3.7-3.2c-.9-1.3-1.4-3-1.4-5h6c.1.8.3 1.6.7 2.2s1 1.2 1.6 1.5c.7.4 1.5.5 2.4.5 1 0 1.8-.2 2.4-.6a4 4 0 0 0 1.6-1.8c.3-.8.5-1.8.5-3V45.5zm30.9 9.1a4.4 4.4 0 0 0-2-3.3 7.5 7.5 0 0 0-4.3-1.1c-1.3 0-2.4.2-3.3.5-.9.4-1.6 1-2 1.6a3.5 3.5 0 0 0-.3 4c.3.5.7.9 1.3 1.2l1.8 1 2 .5 3.2.8c1.3.3 2.5.7 3.7 1.2a13 13 0 0 1 3.2 1.8 8.1 8.1 0 0 1 3 6.5c0 2-.5 3.7-1.5 5.1a10 10 0 0 1-4.4 3.5c-1.8.8-4.1 1.2-6.8 1.2-2.6 0-4.9-.4-6.8-1.2-2-.8-3.4-2-4.5-3.5a10 10 0 0 1-1.7-5.6h6a5 5 0 0 0 3.5 4.6c1 .4 2.2.6 3.4.6 1.3 0 2.5-.2 3.5-.6 1-.4 1.8-1 2.4-1.7a4 4 0 0 0 .8-2.4c0-.9-.2-1.6-.7-2.2a11 11 0 0 0-2.1-1.4l-3.2-1-3.8-1c-2.8-.7-5-1.7-6.6-3.2a7.2 7.2 0 0 1-2.4-5.7 8 8 0 0 1 1.7-5 10 10 0 0 1 4.3-3.5c2-.8 4-1.2 6.4-1.2 2.3 0 4.4.4 6.2 1.2 1.8.8 3.2 2 4.3 3.4 1 1.4 1.5 3 1.5 5h-5.8z"/></svg>

    File: tts-demo/public/vercel.svg
    + <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 283 64"><path fill="black" d="M141 16c-11 0-19 7-19 18s9 18 20 18c7 0 13-3 16-7l-7-5c-2 3-6 4-9 4-5 0-9-3-10-7h28v-3c0-11-8-18-19-18zm-9 15c1-4 4-7 9-7s8 3 9 7h-18zm117-15c-11 0-19 7-19 18s9 18 20 18c6 0 12-3 16-7l-8-5c-2 3-5 4-8 4-5 0-9-3-11-7h28l1-3c0-11-8-18-19-18zm-10 15c2-4 5-7 10-7s8 3 9 7h-19zm-39 3c0 6 4 10 10 10 4 0 7-2 9-5l8 5c-3 5-9 8-17 8-11 0-19-7-19-18s8-18 19-18c8 0 14 3 17 8l-8 5c-2-3-5-5-9-5-6 0-10 4-10 10zm83-29v46h-9V5h9zM37 0l37 64H0L37 0zm92 5-27 48L74 5h10l18 30 17-30h10zm59 12v10l-3-1c-6 0-10 4-10 10v15h-9V17h9v9c0-5 6-9 13-9z"/></svg>

    File: tts-demo/styles/ErrorPopup.module.css
    + .container {
    +     position: fixed;
    +     top: 0;
    +     left: 0;
    +     width: 100%;
    +     height: 100%;
    +     display: flex;
    +     justify-content: center;
    +     align-items: center;
    +     background-color: rgba(0, 0, 0, 0.5);
    +     z-index: 9999;
    +   }
    + 
    + 
    +   
    +   .content {
    +     text-align: center;
    +     background-color: #fff;
    +     padding: 2rem;
    +     border-radius: 0.25rem;
    +   }
    +   
    +   .content > p {
    +     font-size: 1.5rem;
    +     font-weight: 600;
    +     color: #333;
    +   }
    +   
    +   .content > button {
    +     margin-top: 1rem;
    +     padding: 0.5rem 1rem;
    +     border: 1px solid #333;
    +     border-radius: 0.25rem;
    +     background-color: #fff;
    +     font-size: 1rem;
    +     font-weight: 600;
    +     color: #333;
    +     cursor: pointer;
    +   }
    +   

    File: tts-demo/styles/Home.module.css
    + .main {
    +   display: flex;
    +   flex-direction: column;
    +   justify-content: space-evenly;
    +   align-items: center;
    +   padding: 6rem;
    +   min-height: 100vh;
    + }
    + 
    + .textHeader {
    +   text-align: center;
    +   display: flex;
    +   flex-direction: column;
    +   align-items: center;
    +   justify-content: center;
    +   gap: 1rem;
    +   max-width: 50%;
    + }
    + 
    + .description {
    +   line-height: 1.5rem;
    + }
    + .container {
    +   padding: 2rem;
    +   border-radius: 6px;
    +   background-color: white;
    +   display: flex;
    +   flex-direction: row;
    +   align-items: center;
    +   gap: 2rem;
    + }
    + .imageContainer {
    +   padding: 1rem;
    +   border-radius: 50%;
    +   border: 1px solid black;
    +   background-color: #f5f5f5;
    +   opacity: 1;
    +   transition: background-color 0.5s ease-in-out;
    + }
    + 
    + 
    + .microphone {
    +   width: 2rem;
    +   height: 2rem;
    +   cursor: pointer;
    +   user-select: none;
    + }
    + 
    + /* target the stroke of the svg */
    + .active {
    +   background-color: tomato;
    +   animation: pulse 2s infinite;
    +   transition: background-color 0.5s ease-in-out;
    + }
    + 
    + @keyframes pulse {
    +   0% {
    +     background-color: #ff6347;
    +     transform: scale(1);
    +   }
    +   50% {
    +     background-color: #ff634750;
    +     transform: scale(1.02);
    +   }
    +   100% {
    +     background-color: #ff6347;
    +     transform: scale(1);
    +   }
    + }
    + 
    + 
    + .text {
    +   color: black;
    +   
    + }
    + 
    + .iterim {
    +   color: #ccc;
    + }
    + 
    + .text::selection {
    +   background-color: #f5f5f5;
    + }

    File: tts-demo/styles/globals.css
    + :root {
    +   --max-width: 1100px;
    +   --border-radius: 12px;
    +   --font-mono: ui-monospace, Menlo, Monaco, 'Cascadia Mono', 'Segoe UI Mono',
    +     'Roboto Mono', 'Oxygen Mono', 'Ubuntu Monospace', 'Source Code Pro',
    +     'Fira Mono', 'Droid Sans Mono', 'Courier New', monospace;
    + 
    +   --foreground-rgb: 0, 0, 0;
    +   --background-start-rgb: 214, 219, 220;
    +   --background-end-rgb: 255, 255, 255;
    + 
    +   --primary-glow: conic-gradient(
    +     from 180deg at 50% 50%,
    +     #16abff33 0deg,
    +     #0885ff33 55deg,
    +     #54d6ff33 120deg,
    +     #0071ff33 160deg,
    +     transparent 360deg
    +   );
    +   --secondary-glow: radial-gradient(
    +     rgba(255, 255, 255, 1),
    +     rgba(255, 255, 255, 0)
    +   );
    + 
    +   --tile-start-rgb: 239, 245, 249;
    +   --tile-end-rgb: 228, 232, 233;
    +   --tile-border: conic-gradient(
    +     #00000080,
    +     #00000040,
    +     #00000030,
    +     #00000020,
    +     #00000010,
    +     #00000010,
    +     #00000080
    +   );
    + 
    +   --callout-rgb: 238, 240, 241;
    +   --callout-border-rgb: 172, 175, 176;
    +   --card-rgb: 180, 185, 188;
    +   --card-border-rgb: 131, 134, 135;
    + }
    + 
    + @media (prefers-color-scheme: dark) {
    +   :root {
    +     --foreground-rgb: 255, 255, 255;
    +     --background-start-rgb: 0, 0, 0;
    +     --background-end-rgb: 0, 0, 0;
    + 
    +     --primary-glow: radial-gradient(rgba(1, 65, 255, 0.4), rgba(1, 65, 255, 0));
    +     --secondary-glow: linear-gradient(
    +       to bottom right,
    +       rgba(1, 65, 255, 0),
    +       rgba(1, 65, 255, 0),
    +       rgba(1, 65, 255, 0.3)
    +     );
    + 
    +     --tile-start-rgb: 2, 13, 46;
    +     --tile-end-rgb: 2, 5, 19;
    +     --tile-border: conic-gradient(
    +       #ffffff80,
    +       #ffffff40,
    +       #ffffff30,
    +       #ffffff20,
    +       #ffffff10,
    +       #ffffff10,
    +       #ffffff80
    +     );
    + 
    +     --callout-rgb: 20, 20, 20;
    +     --callout-border-rgb: 108, 108, 108;
    +     --card-rgb: 100, 100, 100;
    +     --card-border-rgb: 200, 200, 200;
    +   }
    + }
    + 
    + * {
    +   box-sizing: border-box;
    +   padding: 0;
    +   margin: 0;
    + }
    + 
    + html,
    + body {
    +   max-width: 100vw;
    +   overflow-x: hidden;
    + }
    + 
    + body {
    +   color: rgb(var(--foreground-rgb));
    +   background: linear-gradient(
    +       to bottom,
    +       transparent,
    +       rgb(var(--background-end-rgb))
    +     )
    +     rgb(var(--background-start-rgb));
    + }
    + 
    + a {
    +   color: inherit;
    +   text-decoration: none;
    + }
    + 
    + @media (prefers-color-scheme: dark) {
    +   html {
    +     color-scheme: dark;
    +   }
    + }


    Code Removed:
        File: .gitignore

    File: tts-demo/.gitignore

    File: tts-demo/README.md

    File: tts-demo/assets/mic.svg

    File: tts-demo/jsconfig.json

    File: tts-demo/modals/ErrorPopup.js

    File: tts-demo/next.config.js

    File: tts-demo/package.json

    File: tts-demo/pages/_app.js

    File: tts-demo/pages/_document.js

    File: tts-demo/pages/api/hello.js

    File: tts-demo/pages/index.js

    File: tts-demo/public/favicon.ico

    File: tts-demo/public/next.svg

    File: tts-demo/public/vercel.svg

    File: tts-demo/styles/ErrorPopup.module.css

    File: tts-demo/styles/Home.module.css

    File: tts-demo/styles/globals.css



### charliemeyer2000: 'documentation on relay & config' @ 06/22/2023, 18:01:10 to assorted-scenthound-things

    Code Added:
        File: notes/scenter-app-learning.md
    + Here's a basic rundown of the tools used (besides the obvious, like `create-react-app`). This includes both the libraries used and other tools. 
    + 1. `yarn` - this uses yarn instead of `npm` for package management, so make sure to run `yarn install` instead of `npm install` when installing packages.
    + 1. `eslint` - used for linting, which is a way to enforce code style and catch bugs. You can see the configuration in `.eslintrc.js`. If you're using VSCode, I would suggest installing the ESLint extension and configuring it to automatically fix on save. I have a custom command for "ESLint: fix all auto-fixable Problems: eslint.executeAutoFix" to do this. 
    +     * Note: You can access the keyboard shortcuts with `cmd + k` and then `cmd + s` and preferences with `cmd + ,` on Mac, or `ctrl + k` and then `ctrl + s` and preferences with `ctrl + ,` on Windows.
    + 1. `react-redux` - library used for state management. In this case, it is used for authentication working with cognito. You can see the redux store and other configuration in the folder `src/redux`. 
    + 1. `craco` - this is used to override the webpack configuration that is used by `create-react-app`. You can see the configuration in `craco.config.js`.
    + 1.  `relay` - this is the library used for GraphQL. You can see the configuration. If you are getting errors when attempting to run `yarn relay:watch` or other relay commands, make sure you have installed `watchman` on your machine. You can do this with `brew install watchman` on Mac or `choco install watchman` on Windows. Read more about specifics of relay & appsync [here](#appsync--updating-the-schema).
    + 
    + ### AppSync & Updating the Schema
    + 
    + The website has to stay up-to-date with the schema in AppSync. To do this, there is a script in the `scripts` folder called `update-appsync.sh` that achieves this, along with various yarn scripts in `package.json` to help you. Below is a high-level outline of what they do and when/how to use them. 
    + 
    + 1. Directly running the `update-appsync.sh` script will update your local schema to the latest version in AppSync. furthermore, there are options to run it in prod or dev. If you specify prod - `update-appsync prod` it updates from the prod environment - if you don't specify, it defaults to dev. 
    +     * This is important to understand the difference between dev and prod, too - there are two different databases. Go to AWS Console and log in (see [Setup and Configuration](#setup--configuration) if you don't have a login). Then, go to AppSync and you'll see two different environments - dev and prod. These are the two different databases. Navigate to "Queries" and you can run queries on the database and poke around to see the schema to validate what exists/what doesn't. 
    +         * To run queries, click _log in with user pools_ and log in as if you were inputting a Location ID and password into the actual app (you're logging in as per). 
    +     * So, when you are running update-appsync.sh, it updates according to the schemas in either the `dev` or `prod` environment that you see in AppSync.
    + 
    + #### When/how to use `update-appsync.sh`
    + 
    + You should run this script whenever you make changes to the schema in AppSync. This is because the schema is used by relay to generate types and other things that are used in the frontend. For example, if you want to display a new field on the frontend, you'd have to add it to the schema and then update your schema. 
    + 
    + There are various commands related to `relay`, including `relay`, `relay:prod` and `relay:watch`. You can look at exactly what's executed in the `package.json` file, but a summary is:
    + 1. `relay` - runs `update-appsync.sh` on the dev environment and starts the relay compiler.
    + 1. `relay:prod` - runs `update-appsync.sh` on the prod environment and starts the relay compiler.
    + 1. `relay:watch` - just runs `relay-compiler --watch` to watch for changes in the schema and update the relay files accordingly.


    Code Removed:
        File: notes/scenter-app-learning.md
    - 
    - Here's a basic rundown of the tools used (besides the obvious, like `create-react-app`).
    - 1. `react-redux` - 



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




