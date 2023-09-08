# Expected goals, visualised.

[*xgvisualised.com*](https://www.xgvisualised.com)  
A data visualisation article with up-to-date stats for every Premier League player.

![image](https://user-images.githubusercontent.com/51888045/233871115-d28e3f34-fd16-4c5c-b50d-bb57c45838fe.png)

## Frontend

Built with [Svelte](https://svelte.dev/) and [SvelteKit](https://kit.svelte.dev/)  
Deployed on [Vercel](https://vercel.com/)

## Backend

Serves as a caching layer for [Understat](https://understat.com/) data (scraped using this [understat python package](https://understat.readthedocs.io/en/latest/))  
API is built with [FastAPI](https://fastapi.tiangolo.com/), using [Redis](https://redis.io/) for caching  
Deployed on a digital ocean droplet
