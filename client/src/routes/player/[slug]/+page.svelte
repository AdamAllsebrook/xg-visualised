<script>
	import GraphXg from '$lib/GraphXg.svelte';
    import { matches, seasons, team } from './store.js';

    export let data;

</script>

<div class="container" style="max-width: 720px">
    <div class="headings">
        <h2>{data.first_name} {data.second_name}</h2>
        <h5>{$team.name}</h5>
    </div>
    <GraphXg matches={$matches}/>
</div>