<script lang='ts'>
    import type { Player } from '$client';

    export let data: Player;

</script>

<div class="container" style="max-width: 720px">
    <div class="headings">
        <h2>{data.player_name}</h2>
        <h5>{data.team_title}</h5>
    </div>
    <a href="/player/{data.id}/xg_story">Go to the xG story.</a>
</div>