<script lang='ts'>
    import type { Player, Match, Shot, Fixture, Team } from '$client';
    import FixtureList from '$lib/FixtureList.svelte';

    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];
    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;

    const nFixtures = 5;

    $: fixturesSlice = fixtures.slice(0, nFixtures);
    const sideSwitch = {h: 'a', a: 'h'};
    let opponents: Team[];
    $: opponents = fixturesSlice.map(d => teams.get(d[sideSwitch[d.side]].title))
    $: averageXGA = (opponents.map(d => d.xGA / d.games).reduce((x,y) => x + y, 0) / nFixtures).toFixed(2);
    function per90(n: number, mins: number) {
        return (n / mins * 90).toFixed(2);
    }

</script>

<h3 class='font-bold text-2xl'>Fixtures</h3>
<p>
    {player.team_title}'s next {nFixtures} games are against:
</p>
<FixtureList
    fixtures={fixtures.slice(0, nFixtures)}
    {teams}
/>
<p>(Hover/ tap for more data)</p>
<br>
<p>
    These teams have an average xGA90 of {averageXGA}.
</p>
<br>
<p>
    Visualised: The combined heatmap of all shots against these teams this season.
</p>
