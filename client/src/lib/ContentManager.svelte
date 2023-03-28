<script lang='ts'>
    import { colours } from '$lib/colours';

    import Intro from './content/Intro.svelte';
    import XgOverview from './content/XgOverview.svelte';
	import FixturesOverview from './content/FixturesOverview.svelte';
	import ShotsInBox from './content/ShotsInBox.svelte';
	import LeftRight from './content/LeftRight.svelte';
	import TimelineIntro from './content/TimelineIntro.svelte';
	import HomeAway from './content/HomeAway.svelte';
	import FirstSecondHalf from './content/FirstSecondHalf.svelte';
	import Padding from './content/Padding.svelte';

    export let currentStep: number;

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
            <svelte:component this={item}/>
        </div>
    </div>
{/each}
