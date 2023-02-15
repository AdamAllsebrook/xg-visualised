import { error, type Load } from '@sveltejs/kit';
import { matches, seasons, team } from './store.js';
import { PlayerService, TeamService } from '$client';

export const load: Load = async ({ params }) => {
    if (!params.slug) throw error(400, 'Must include a player ID.');
    let id = parseInt(params.slug);

    const player = await PlayerService.playerRead(id);
    PlayerService.playerReadMatches(id)
        .then(data => matches.set(data));
    PlayerService.playerReadSeasons(id)
        .then(data => seasons.set(data));
    // // PlayerService.playerReadShots(id)
    //     .then(data => shots.set(data));
    TeamService.teamRead(player.team)
        .then(data => team.set(data));
    return player;

    // if (res.ok) {
    //     fetch('http://localhost:8000/player/' + params.slug + '/matches')
    //         .then(res => res.json())
    //         .then(data => matches.set(data))
    //         .catch(e => matches.set([]));
    //     fetch('http://localhost:8000/player/' + params.slug + '/seasons')
    //         .then(res => res.json())
    //         .then(data => seasons.set(data))
    //         .catch(e => seasons.set([]));

    //     let data = await res.json();
    //     fetch('http://localhost:8000/team/' + data.team)
    //         .then(res => res.json())
    //         .then(data => team.set(data))
    //         .catch();
    //     return data;
    // }
    // else
    //     throw error(res.status, res.statusText);
}