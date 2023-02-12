import { error } from '@sveltejs/kit';
import { matches, seasons, team } from './store.js';

export async function load({ fetch, params }) {
    const res = await fetch('http://localhost:8000/player/' + params.slug)
    if (res.ok) {
        fetch('http://localhost:8000/player/' + params.slug + '/matches')
            .then(res => res.json())
            .then(data => matches.set(data))
            .catch(e => matches.set([]));
        fetch('http://localhost:8000/player/' + params.slug + '/seasons')
            .then(res => res.json())
            .then(data => seasons.set(data))
            .catch(e => seasons.set([]));

        let data = await res.json();
        fetch('http://localhost:8000/team/' + data.team)
            .then(res => res.json())
            .then(data => team.set(data))
            .catch();
        return data;
    }
    else
        throw error(res.status, res.statusText);
}