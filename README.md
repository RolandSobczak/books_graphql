<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RolandSobczak/books_graphql">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/GraphQL_Logo.svg/220px-GraphQL_Logo.svg.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">GraphQL - books</h3>

  <p align="center">
    Simple GraphQL API implemented with Strawberry and FastAPI
    <br />
    <a href="https://github.com/RolandSobczak/books_graphql"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/RolandSobczak/books_graphql">View Demo</a>
    ·
    <a href="https://github.com/RolandSobczak/books_graphql/issues">Report Bug</a>
    ·
    <a href="https://github.com/RolandSobczak/books_graphql/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li>
        <a href="#usage">Usage</a>
        <ul>
            <li><a href="#how-to-get-demo-data">How to get demo data</a></li>
        </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#what-i-have-learned">What I have learned</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![Postgres][Postgres]][Postgres-url]
* [![GraphQL][GraphQL]][GraphQL-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/RolandSobczak/books_graphql.git
   ```
2. Copy .env examples files from `/env/examples/` info `env/` and remove sufix `.example`
3. Build image
   ```shell
   docker-compose build
   ```
4. Run the project
   ```shell
   docker-compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Open `http//localhost:8000/graphql` in browser or postman


### How to get demo data

I have prepared bunch of data generation commands using Factory Boy

How to use it?:
```shell
docker-compose run backend poetry run create-authors -c 100
```

Here is the list of available commands:

- create-books
- create-authors
- create-users



<!-- ROADMAP -->
## Roadmap

- [x] GrapQL API
  - [x] Book resource
  - [x] Author resource
  - [x] User resource
- [x] Auth
  - [x] JWT auth
  - [x] Permissions
- [x] Docs

See the [open issues](https://github.com/RolandSobczak/books_graphql/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## What I have learned?

1. How to use GraphQL API 
2. How to implement GraphQL API using Strawberry framework
3. Better code organization using Services approach
4. Better SqlAlchemy session management using Borg pattern

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Roland Sobczak - [@linkedin_handle](https://www.linkedin.com/in/roland-sobczak/) - rolandsobczak@icloud.com

Project Link: [https://github.com/RolandSobczak/books_graphql](https://github.com/RolandSobczak/books_graphql)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Strawberry docs](https://strawberry.rocks)
* [FastAPI docs](https://fastapi.tiangolo.com)
* [SqlAlchemy](https://www.sqlalchemy.org)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/RolandSobczak/books_graphql/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/RolandSobczak/books_graphql/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/RolandSobczak/books_graphql/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/RolandSobczak/books_graphql/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/RolandSobczak/books_graphql/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/roland-sobczak/

[product-screenshot]: docs/screenshot.png
[Python]: https://img.shields.io/badge/Python-FFFFFF?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org
[FastAPI]: https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com
[GraphQL]: https://img.shields.io/badge/GraphQl-E10098?style=for-the-badge&logo=graphql&logoColor=white
[GraphQL-url]: https://graphql.org/
[Postgres]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Docker]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://hub.docker.com/
