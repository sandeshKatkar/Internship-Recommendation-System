"""
roadmap_data.py - Learning roadmaps for all 14 internship domains.
Each domain has phases with skills, resources, and timelines.
"""

ROADMAPS = {
    "Machine Learning Engineer": {
        "icon": "🤖",
        "description": "Build intelligent systems that learn from data and make predictions.",
        "phases": [
            {
                "title": "Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Python Programming", "resource": "Python.org / Automate the Boring Stuff"},
                    {"name": "Mathematics (Linear Algebra, Calculus)", "resource": "Khan Academy / 3Blue1Brown"},
                    {"name": "Statistics & Probability", "resource": "StatQuest with Josh Starmer"},
                    {"name": "NumPy & Pandas", "resource": "Kaggle Learn / Official Docs"},
                ]
            },
            {
                "title": "Core ML Skills",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Scikit-learn (Classical ML)", "resource": "Scikit-learn Docs / Coursera ML"},
                    {"name": "Data Preprocessing & Feature Engineering", "resource": "Kaggle Competitions"},
                    {"name": "Model Evaluation & Cross Validation", "resource": "ML Mastery Blog"},
                    {"name": "Matplotlib & Seaborn Visualization", "resource": "Official Docs / Real Python"},
                ]
            },
            {
                "title": "Advanced & Specialization",
                "duration": "3-4 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Deep Learning (TensorFlow/PyTorch)", "resource": "fast.ai / DeepLearning.AI"},
                    {"name": "Natural Language Processing", "resource": "Hugging Face Course"},
                    {"name": "MLOps & Model Deployment", "resource": "MLflow / BentoML Docs"},
                    {"name": "Build 3+ Portfolio Projects", "resource": "Kaggle / GitHub"},
                ]
            }
        ]
    },
    "Data Scientist": {
        "icon": "📊",
        "description": "Extract insights from complex data to drive business decisions.",
        "phases": [
            {
                "title": "Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Python & R Basics", "resource": "DataCamp / Codecademy"},
                    {"name": "Statistics & Hypothesis Testing", "resource": "StatQuest / Khan Academy"},
                    {"name": "SQL for Data Analysis", "resource": "Mode Analytics / SQLZoo"},
                    {"name": "Excel & Data Cleaning", "resource": "Excel Jet / YouTube Tutorials"},
                ]
            },
            {
                "title": "Core Data Skills",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Exploratory Data Analysis (EDA)", "resource": "Kaggle Learn / Towards Data Science"},
                    {"name": "Machine Learning Fundamentals", "resource": "Coursera ML / Scikit-learn Docs"},
                    {"name": "Data Visualization (Tableau/Power BI)", "resource": "Tableau Public / Microsoft Learn"},
                    {"name": "A/B Testing & Experimentation", "resource": "Udacity / Medium Articles"},
                ]
            },
            {
                "title": "Advanced Analytics",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Big Data (Spark, Hadoop)", "resource": "Databricks Community / Udemy"},
                    {"name": "Time Series Analysis", "resource": "Forecasting PnP / Prophet Docs"},
                    {"name": "Business Storytelling", "resource": "Storytelling with Data Book"},
                    {"name": "Portfolio with Real Datasets", "resource": "Kaggle / UCI ML Repository"},
                ]
            }
        ]
    },
    "Software Developer": {
        "icon": "💻",
        "description": "Design and build software applications and systems.",
        "phases": [
            {
                "title": "Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Core Programming (Python/Java/C++)", "resource": "LeetCode / HackerRank"},
                    {"name": "Data Structures & Algorithms", "resource": "Abdul Bari / GeeksForGeeks"},
                    {"name": "Git & Version Control", "resource": "Pro Git Book / GitHub Docs"},
                    {"name": "Linux Basics", "resource": "Linux Journey / The Missing Semester"},
                ]
            },
            {
                "title": "Software Engineering",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "DBMS & SQL", "resource": "CS50 SQL / MySQL Docs"},
                    {"name": "OOP Design Patterns", "resource": "Refactoring Guru / Head First Design Patterns"},
                    {"name": "REST APIs", "resource": "REST API Tutorial / Postman Learning"},
                    {"name": "Testing (Unit, Integration)", "resource": "PyTest Docs / JUnit"},
                ]
            },
            {
                "title": "Professional Skills",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "System Design", "resource": "Grokking System Design / ByteByteGo"},
                    {"name": "Agile & Scrum", "resource": "Atlassian Agile Coach"},
                    {"name": "Cloud Basics (AWS/Azure)", "resource": "AWS Free Tier / AZ-900"},
                    {"name": "Build & Deploy Projects", "resource": "GitHub / Heroku / Vercel"},
                ]
            }
        ]
    },
    "Python Developer": {
        "icon": "🐍",
        "description": "Build applications, automation, and web services using Python.",
        "phases": [
            {
                "title": "Python Mastery",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Advanced Python (OOP, Generators, Decorators)", "resource": "Real Python / Python Docs"},
                    {"name": "Data Structures & Algorithms in Python", "resource": "LeetCode / Corey Schafer YouTube"},
                    {"name": "Virtual Environments & pip", "resource": "Python Packaging Guide"},
                    {"name": "File Handling, JSON, CSV", "resource": "Automate the Boring Stuff"},
                ]
            },
            {
                "title": "Web & Frameworks",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Flask or Django", "resource": "Flask Docs / Django Girls Tutorial"},
                    {"name": "REST API Development", "resource": "FastAPI Docs / DRF Tutorial"},
                    {"name": "Database Integration (SQLAlchemy, SQLite)", "resource": "SQLAlchemy Docs"},
                    {"name": "Testing (PyTest)", "resource": "PyTest Official Docs"},
                ]
            },
            {
                "title": "Automation & Deployment",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Web Scraping (BeautifulSoup, Selenium)", "resource": "Scrapy Docs / Real Python"},
                    {"name": "Automation Scripts", "resource": "Automate with Python / PyCon Talks"},
                    {"name": "Docker & Deployment", "resource": "Docker Docs / Heroku"},
                    {"name": "Build 3+ Python Projects", "resource": "GitHub / Python.org Project Ideas"},
                ]
            }
        ]
    },
    "Java Developer": {
        "icon": "☕",
        "description": "Build robust enterprise applications and backend services with Java.",
        "phases": [
            {
                "title": "Java Core",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Core Java (OOP, Collections, Exceptions)", "resource": "Java Brains / Head First Java"},
                    {"name": "Data Structures & Algorithms", "resource": "GeeksForGeeks / LeetCode"},
                    {"name": "JVM & Memory Management", "resource": "Java Performance Book"},
                    {"name": "Maven / Gradle Build Tools", "resource": "Official Docs"},
                ]
            },
            {
                "title": "Enterprise Java",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Spring Boot Framework", "resource": "Spring.io Official / Baeldung"},
                    {"name": "Hibernate & JPA (ORM)", "resource": "Hibernate Docs / Baeldung"},
                    {"name": "REST APIs with Spring", "resource": "Spring Boot REST Tutorial"},
                    {"name": "JUnit Testing", "resource": "JUnit 5 Docs / Testing with Spring"},
                ]
            },
            {
                "title": "Advanced & Cloud",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Microservices Architecture", "resource": "Spring Cloud Docs / Sam Newman Book"},
                    {"name": "Kafka & Message Queues", "resource": "Confluent Docs / YouTube"},
                    {"name": "Docker & Kubernetes", "resource": "Docker Docs / K8s Docs"},
                    {"name": "Build Enterprise Projects", "resource": "GitHub / IntelliJ Projects"},
                ]
            }
        ]
    },
    "Frontend Developer": {
        "icon": "🎨",
        "description": "Create beautiful, interactive user interfaces for web applications.",
        "phases": [
            {
                "title": "Web Fundamentals",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "HTML5 Semantic Elements", "resource": "MDN Web Docs / freeCodeCamp"},
                    {"name": "CSS3 (Flexbox, Grid, Animations)", "resource": "CSS-Tricks / Scrimba"},
                    {"name": "JavaScript ES6+", "resource": "javascript.info / Eloquent JavaScript"},
                    {"name": "Responsive Design", "resource": "Google Developers / Kevin Powell YouTube"},
                ]
            },
            {
                "title": "Frameworks & Tools",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "React.js", "resource": "React Docs / Scrimba React"},
                    {"name": "State Management (Redux / Context)", "resource": "Redux Docs / Traversy Media"},
                    {"name": "REST API Integration (Fetch/Axios)", "resource": "JavaScript.info / YouTube"},
                    {"name": "Git & GitHub", "resource": "Pro Git / GitHub Docs"},
                ]
            },
            {
                "title": "Advanced Frontend",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "TypeScript", "resource": "TypeScript Docs / Matt Pocock"},
                    {"name": "Testing (Jest, Testing Library)", "resource": "Testing Library Docs / Kent C. Dodds"},
                    {"name": "Performance & Accessibility", "resource": "web.dev / Lighthouse"},
                    {"name": "Build & Deploy Portfolio", "resource": "Vercel / Netlify / GitHub Pages"},
                ]
            }
        ]
    },
    "Backend Developer": {
        "icon": "⚙️",
        "description": "Build scalable server-side logic, APIs, and databases.",
        "phases": [
            {
                "title": "Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Server-Side Language (Node.js / Python / Java)", "resource": "Node.js Docs / Flask Docs"},
                    {"name": "SQL & Relational Databases", "resource": "CS50 SQL / PostgreSQL Docs"},
                    {"name": "HTTP & REST Principles", "resource": "REST API Tutorial / MDN"},
                    {"name": "Git & Version Control", "resource": "Pro Git Book"},
                ]
            },
            {
                "title": "API & Database Skills",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "RESTful API Design", "resource": "Swagger / Postman / OpenAPI"},
                    {"name": "Authentication (JWT, OAuth)", "resource": "JWT.io / Auth0 Docs"},
                    {"name": "NoSQL (MongoDB, Redis)", "resource": "MongoDB University / Redis Docs"},
                    {"name": "ORM Tools", "resource": "SQLAlchemy / Sequelize / TypeORM Docs"},
                ]
            },
            {
                "title": "Scalability & DevOps",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Caching (Redis, Memcached)", "resource": "Redis Docs / Cloudflare Blog"},
                    {"name": "Message Queues (RabbitMQ, Kafka)", "resource": "CloudAMQP Docs"},
                    {"name": "Docker & Containerization", "resource": "Docker Docs / TechWorld with Nana"},
                    {"name": "Build Scalable API Projects", "resource": "GitHub / Render / Railway"},
                ]
            }
        ]
    },
    "Full Stack Developer": {
        "icon": "🌐",
        "description": "Build complete web applications from frontend to backend.",
        "phases": [
            {
                "title": "Frontend Basics",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "HTML, CSS, JavaScript", "resource": "freeCodeCamp / The Odin Project"},
                    {"name": "React or Vue.js", "resource": "React Docs / Vue Mastery"},
                    {"name": "Responsive Design & CSS Frameworks", "resource": "Tailwind Docs / Bootstrap"},
                    {"name": "Git & GitHub Workflow", "resource": "GitHub Docs"},
                ]
            },
            {
                "title": "Backend & Database",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Backend Framework (Node/Express or Flask)", "resource": "Express Docs / Flask Docs"},
                    {"name": "Database Design (SQL + NoSQL)", "resource": "CS50 / MongoDB University"},
                    {"name": "REST API Development", "resource": "Postman / Swagger Docs"},
                    {"name": "Authentication & Authorization", "resource": "JWT / Passport.js Docs"},
                ]
            },
            {
                "title": "Deployment & Advanced",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Docker & CI/CD Pipelines", "resource": "Docker Docs / GitHub Actions"},
                    {"name": "Cloud Deployment (AWS/Vercel/Render)", "resource": "AWS Free Tier / Vercel Docs"},
                    {"name": "System Design Basics", "resource": "ByteByteGo / Grokking System Design"},
                    {"name": "Build Full Stack Projects", "resource": "GitHub Portfolio / Hashnode Blog"},
                ]
            }
        ]
    },
    "Data Analyst": {
        "icon": "📈",
        "description": "Analyze data to discover trends and help organizations make data-driven decisions.",
        "phases": [
            {
                "title": "Analytics Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Excel & Google Sheets", "resource": "Excel Jet / Chandoo.org"},
                    {"name": "SQL for Data Querying", "resource": "Mode Analytics / SQLZoo / DataCamp"},
                    {"name": "Statistics for Data Analysis", "resource": "Khan Academy / StatQuest"},
                    {"name": "Python Basics (Pandas, NumPy)", "resource": "Kaggle Learn Python"},
                ]
            },
            {
                "title": "Visualization & Tools",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Power BI or Tableau", "resource": "Microsoft Learn / Tableau Public"},
                    {"name": "Python Data Viz (Matplotlib, Seaborn, Plotly)", "resource": "Real Python / Plotly Docs"},
                    {"name": "Exploratory Data Analysis", "resource": "Kaggle Notebooks / Towards Data Science"},
                    {"name": "Data Storytelling", "resource": "Storytelling with Data / Cole Nussbaumer"},
                ]
            },
            {
                "title": "Advanced Analytics",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Advanced SQL (Window Functions, CTEs)", "resource": "Mode Analytics / LeetCode SQL"},
                    {"name": "A/B Testing & Metrics", "resource": "Udacity Experiments / Medium"},
                    {"name": "Business Intelligence Concepts", "resource": "Google Analytics / BI courses"},
                    {"name": "Portfolio with Business Datasets", "resource": "Kaggle / World Bank Data"},
                ]
            }
        ]
    },
    "Cloud Engineer": {
        "icon": "☁️",
        "description": "Design, build, and manage cloud infrastructure and services.",
        "phases": [
            {
                "title": "Cloud Fundamentals",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Linux & Networking Basics", "resource": "Linux Journey / CompTIA Network+"},
                    {"name": "AWS/Azure/GCP Fundamentals", "resource": "AWS Free Tier / AZ-900 / GCP ACE"},
                    {"name": "Cloud Compute & Storage", "resource": "Official Cloud Docs"},
                    {"name": "Virtualization Concepts", "resource": "VMware / VirtualBox Tutorials"},
                ]
            },
            {
                "title": "Infrastructure & DevOps",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Docker & Containerization", "resource": "Docker Docs / TechWorld with Nana"},
                    {"name": "Kubernetes (K8s)", "resource": "Kubernetes Docs / KodeKloud"},
                    {"name": "Terraform (IaC)", "resource": "HashiCorp Learn / Terraform Docs"},
                    {"name": "CI/CD Pipelines (GitHub Actions)", "resource": "GitHub Actions Docs / Jenkins"},
                ]
            },
            {
                "title": "Cloud Architecture",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Cloud Security & IAM", "resource": "AWS Security / Microsoft Defender"},
                    {"name": "Serverless Computing", "resource": "AWS Lambda / Azure Functions Docs"},
                    {"name": "Cost Optimization", "resource": "AWS Well-Architected / GCP Cost Docs"},
                    {"name": "Cloud Certifications (AWS SAA / AZ-104)", "resource": "A Cloud Guru / Whizlabs"},
                ]
            }
        ]
    },
    "DevOps Engineer": {
        "icon": "🔄",
        "description": "Bridge development and operations to enable fast, reliable software delivery.",
        "phases": [
            {
                "title": "Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Linux System Administration", "resource": "The Linux Command Line / Linux Journey"},
                    {"name": "Git & Version Control Workflows", "resource": "Atlassian Git Tutorials / Pro Git"},
                    {"name": "Scripting (Bash / Python)", "resource": "Bash Guide / Automate the Boring Stuff"},
                    {"name": "Networking Fundamentals", "resource": "CompTIA Network+ / Cisco NetAcad"},
                ]
            },
            {
                "title": "DevOps Core",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Docker & Container Orchestration", "resource": "Docker Docs / Kubernetes Docs"},
                    {"name": "CI/CD (Jenkins, GitHub Actions, GitLab CI)", "resource": "Jenkins Docs / GitHub Actions"},
                    {"name": "Configuration Management (Ansible)", "resource": "Ansible Docs / TechWorld with Nana"},
                    {"name": "Cloud Platform (AWS/Azure/GCP)", "resource": "Cloud Free Tiers"},
                ]
            },
            {
                "title": "Advanced DevOps",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Infrastructure as Code (Terraform)", "resource": "HashiCorp Learn"},
                    {"name": "Monitoring (Prometheus, Grafana)", "resource": "Grafana Labs / Prometheus Docs"},
                    {"name": "Site Reliability Engineering", "resource": "Google SRE Book (free online)"},
                    {"name": "Security in DevOps (DevSecOps)", "resource": "OWASP / Snyk Docs"},
                ]
            }
        ]
    },
    "Cyber Security Analyst": {
        "icon": "🛡️",
        "description": "Protect systems, networks, and data from digital attacks and threats.",
        "phases": [
            {
                "title": "Security Basics",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Networking (TCP/IP, DNS, HTTP)", "resource": "Professor Messer / CompTIA Net+"},
                    {"name": "Operating Systems (Linux, Windows)", "resource": "TryHackMe / OverTheWire"},
                    {"name": "Cybersecurity Fundamentals", "resource": "Google Cybersecurity Certificate / CompTIA Sec+"},
                    {"name": "Cryptography Basics", "resource": "Crypto101 / Khan Academy"},
                ]
            },
            {
                "title": "Security Skills",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Ethical Hacking & Penetration Testing", "resource": "TryHackMe / HackTheBox"},
                    {"name": "Web Application Security (OWASP Top 10)", "resource": "PortSwigger Web Security Academy"},
                    {"name": "Security Tools (Wireshark, Nmap, Metasploit)", "resource": "Offensive Security / TryHackMe"},
                    {"name": "Incident Response", "resource": "SANS Institute / Blue Team Labs"},
                ]
            },
            {
                "title": "Advanced Security",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "SIEM Tools (Splunk, ELK Stack)", "resource": "Splunk Training / Elastic Docs"},
                    {"name": "Cloud Security", "resource": "AWS Security / Azure Security Center"},
                    {"name": "Security Certifications (CEH, OSCP, Sec+)", "resource": "EC-Council / Offensive Security"},
                    {"name": "CTF Challenges & Bug Bounty", "resource": "HackTheBox / Bugcrowd"},
                ]
            }
        ]
    },
    "Data Engineer": {
        "icon": "🔧",
        "description": "Build and maintain data pipelines, warehouses, and infrastructure.",
        "phases": [
            {
                "title": "Foundation",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Python for Data Engineering", "resource": "Real Python / DataCamp"},
                    {"name": "Advanced SQL & Database Design", "resource": "Mode Analytics / PostgreSQL Docs"},
                    {"name": "Linux & Shell Scripting", "resource": "Linux Journey / Bash Guide"},
                    {"name": "Git & Project Management", "resource": "GitHub Docs / Jira Basics"},
                ]
            },
            {
                "title": "Data Pipeline Tools",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Apache Spark & PySpark", "resource": "Databricks Community / Spark Docs"},
                    {"name": "Apache Airflow (Orchestration)", "resource": "Astronomer.io / Airflow Docs"},
                    {"name": "Kafka (Streaming Data)", "resource": "Confluent Docs / Kafka Tutorials"},
                    {"name": "Cloud Data Services (AWS S3, Redshift)", "resource": "AWS Docs / Google BigQuery"},
                ]
            },
            {
                "title": "Data Warehouse & Advanced",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Data Warehouse Design (Star/Snowflake Schema)", "resource": "Kimball Group / dbt Docs"},
                    {"name": "dbt (Data Build Tool)", "resource": "dbt Labs / Jaffle Shop Tutorial"},
                    {"name": "Data Lakehouse (Delta Lake, Iceberg)", "resource": "Databricks / Apache Iceberg Docs"},
                    {"name": "Build End-to-End Pipeline Projects", "resource": "GitHub / Medium DE Articles"},
                ]
            }
        ]
    },
    "QA/Test Engineer": {
        "icon": "✅",
        "description": "Ensure software quality through systematic testing and quality assurance.",
        "phases": [
            {
                "title": "Testing Fundamentals",
                "duration": "1-2 months",
                "color": "#2D6A4F",
                "skills": [
                    {"name": "Software Testing Concepts (SDLC, STLC)", "resource": "ISTQB Foundation / Guru99"},
                    {"name": "Manual Testing Techniques", "resource": "Software Testing Help / Guru99"},
                    {"name": "Bug Tracking Tools (Jira, Bugzilla)", "resource": "Atlassian Jira Tutorials"},
                    {"name": "SQL for Test Data Validation", "resource": "SQLZoo / Mode Analytics"},
                ]
            },
            {
                "title": "Test Automation",
                "duration": "2-3 months",
                "color": "#40916C",
                "skills": [
                    {"name": "Selenium WebDriver (Python/Java)", "resource": "Selenium Docs / Test Automation University"},
                    {"name": "API Testing (Postman, REST Assured)", "resource": "Postman Learning / Test Automation Uni"},
                    {"name": "PyTest / JUnit", "resource": "PyTest Docs / JUnit 5 Guide"},
                    {"name": "Test Frameworks (Page Object Model)", "resource": "SeleniumHQ / Automation Panda"},
                ]
            },
            {
                "title": "Advanced QA",
                "duration": "2-3 months",
                "color": "#F4A300",
                "skills": [
                    {"name": "Performance Testing (JMeter, Gatling)", "resource": "Apache JMeter / Gatling Docs"},
                    {"name": "CI/CD for Testing (GitHub Actions)", "resource": "GitHub Actions / Jenkins Docs"},
                    {"name": "Mobile Testing (Appium)", "resource": "Appium Docs / Test Automation University"},
                    {"name": "ISTQB Certification", "resource": "ISTQB Official / TMap Docs"},
                ]
            }
        ]
    }
}

# Skill thresholds required for each domain (skills rated 1-10)
DOMAIN_SKILL_REQUIREMENTS = {
    "Machine Learning Engineer": {
        "Python Skill": 7, "Machine Learning": 7, "Deep Learning": 6,
        "Statistics": 6, "Data Analysis": 6, "Algorithms": 6, "Data Structures": 6
    },
    "Data Scientist": {
        "Python Skill": 6, "Statistics": 7, "Data Analysis": 7,
        "Machine Learning": 6, "Data Visualization": 6, "SQL Skill": 5
    },
    "Software Developer": {
        "Data Structures": 7, "Algorithms": 7, "Problem Solving": 7,
        "Software Engineering": 6, "DBMS": 5
    },
    "Python Developer": {
        "Python Skill": 8, "Data Structures": 6, "Algorithms": 6,
        "Software Engineering": 5, "DBMS": 4
    },
    "Java Developer": {
        "Java Skill": 8, "Data Structures": 7, "Algorithms": 7,
        "Software Engineering": 6, "DBMS": 5, "Operating System": 5
    },
    "Frontend Developer": {
        "JavaScript Skill": 7, "Problem Solving": 6, "Data Visualization": 5,
        "Communication": 6, "Software Engineering": 5
    },
    "Backend Developer": {
        "Python Skill": 6, "SQL Skill": 6, "DBMS": 6,
        "Data Structures": 6, "Algorithms": 6, "Software Engineering": 6
    },
    "Full Stack Developer": {
        "JavaScript Skill": 7, "Python Skill": 5, "SQL Skill": 6,
        "DBMS": 6, "Software Engineering": 7, "Problem Solving": 7
    },
    "Data Analyst": {
        "SQL Skill": 7, "Statistics": 6, "Data Analysis": 7,
        "Data Visualization": 7, "Python Skill": 5
    },
    "Cloud Engineer": {
        "AWS": 7, "Azure": 6, "Docker": 7, "Kubernetes": 6,
        "Linux/Operating System": 6, "Computer Networks": 6
    },
    "DevOps Engineer": {
        "Docker": 7, "Kubernetes": 6, "CI/CD": 7,
        "AWS": 6, "Operating System": 7, "Computer Networks": 6
    },
    "Cyber Security Analyst": {
        "Computer Networks": 8, "Operating System": 7,
        "Problem Solving": 7, "Python Skill": 5
    },
    "Data Engineer": {
        "Python Skill": 7, "SQL Skill": 8, "Data Structures": 6,
        "AWS": 6, "DBMS": 7, "Statistics": 5
    },
    "QA/Test Engineer": {
        "Python Skill": 5, "SQL Skill": 5, "Problem Solving": 7,
        "Software Engineering": 6, "Algorithms": 5
    }
}
