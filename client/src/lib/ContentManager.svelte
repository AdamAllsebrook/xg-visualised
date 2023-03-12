<script lang='ts'>
    import type { Player, Shot, Match, SimpleShot, Fixture, Team} from '$client';
    import { colours } from '$lib/colours';

    import Intro from '$lib/content/Intro.svelte';

    export let currentStep: number;
    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];
    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;
    export let allShotsAgainst: Record<string, SimpleShot[]>;

    const content = [
        Intro,
        Intro,
        Intro,
    ];
</script>

{#each content as item, i}
    <div 
        class='h-[85vh] flex place-items-center justify-center lg:block lg:w-3/5' 
        class:active={currentStep === i}
    >
        <div 
            class='p-8 w-full z-10 text-stone-100 font-display'
            style='background: linear-gradient(0deg, {colours.primary}33 0%, {colours.primary}ee 20%, {colours.primary}ee 80%, {colours.primary}33 100%)'
        >
            <svelte:component this={item} {player} {shots} {matches} {fixtures} {teams}/>
        </div>
    </div>
{/each}
