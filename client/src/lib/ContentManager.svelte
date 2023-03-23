<script lang='ts'>
    import type { Writable } from 'svelte/store';
    import { colours } from '$lib/colours';

    import Intro from './content/Intro.svelte';
    import XgOverview from './content/XgOverview.svelte';
	import FixturesOverview from './content/FixturesOverview.svelte';
	import ShotsInBox from './content/ShotsInBox.svelte';
	import { getContext } from 'svelte';
	import LeftRight from './content/LeftRight.svelte';
	import TimelineIntro from './content/TimelineIntro.svelte';
	import HomeAway from './content/HomeAway.svelte';
	import FirstSecondHalf from './content/FirstSecondHalf.svelte';
	import Padding from './content/Padding.svelte';
    import { key as dataKey, type DataManager } from './data/dataManager';
    import type { SimpleShot, Team } from '$client';

    export let currentStep: number;
    let allShotsAgainst: Writable<Record<string, SimpleShot[]> | null> = getContext('allShotsAgainst');

    const dataManager: DataManager = getContext(dataKey);
    const teams = dataManager.teams;
    const fixtures = dataManager.fixtures;

    const nFixtures = 5;
    const sideSwitch = {h: 'a', a: 'h'};
    let opponents: Team[];
    $: opponents = fixtures.slice(0, nFixtures).map(d => teams.get(d[sideSwitch[d.side]].title))
    $: opponentsNames = opponents.map(d => d.title);
    $: allShotsAgainstFixtures = $allShotsAgainst == null ? [] :
        Object.keys($allShotsAgainst).filter(key => opponentsNames.includes(key)).reduce((arr, key) => arr.concat($allShotsAgainst[key]), []);

    const content = [
        Intro,
        XgOverview,
        FixturesOverview,
        ShotsInBox,
        LeftRight,
        TimelineIntro,
        HomeAway,
        FirstSecondHalf,
        Padding
    ];
</script>

{#each content as item, i}
    <div 
        class='h-[100vh] lg:h-[60vh] flex place-items-center justify-center lg:block lg:w-3/5' 
        class:active={currentStep === i}
    >
        <div 
            class='p-8 w-full z-10 text-stone-100 font-display'
            style='background: linear-gradient(0deg, {colours.primary}33 0%, {colours.primary}ee 20%, {colours.primary}ee 80%, {colours.primary}33 100%)'
        >
            <svelte:component this={item} {nFixtures} {allShotsAgainstFixtures}/>
        </div>
    </div>
{/each}
