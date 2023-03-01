<script lang='ts'>
    import { onMount } from 'svelte';
    import { PlayerService } from '$client';
    import type { Player, Match, Season, Shot } from '$client';
    import { scaleLinear } from 'd3-scale';
    import Scrolly from "$lib/Scrolly.svelte";
    import Pitch from './visualise/Pitch.svelte';
    import Matches from './visualise/Matches.svelte';
    import type { Spring } from 'svelte/motion';
    import Tooltip from '$lib/Tooltip.svelte';

    import Intro from './content/Intro.svelte';

    export let data: Player;
    let matches: Match[] = [];
    let seasons: Season[] = [];
    let shots: Shot[] = [];
    let isLoadingShots = true;
    let isLoadingMatches = true;

    let currentStep: number;

    let screenWidth: number;
    let screenHeight: number;
    let containerWidth = 400;
    $: width = screenWidth >= 1024 ? containerWidth * 2/5 : (screenWidth < 480 ? containerWidth * 1.25 : containerWidth);
    $: margin = { top: width*0.04, right: screenWidth >= 1024 ? 32 : 5, left: 32 + (width > containerWidth ? containerWidth - width : 0), bottom: 0 };
    $: height = screenHeight * 0.8;
    $: rScale = scaleLinear()
        .domain([0, 1])
        .range([Math.max(1, width*0.005), width*0.03])

    let tweenedX: Spring<any>;
    let tweenedY: Spring<any>;

    $: tweenedData = shots.map((shot, index) => ({
        x: tweenedX ? $tweenedX[index] : 0,
        y: tweenedY ? $tweenedY[index] : 0
    }));

    let hoveredData: any[] | null;
    let svg;

    $: content = [
        Intro,
        Intro,
        Intro,
    ]

    onMount(async () => {
        PlayerService.playerReadMatches(data.id)
            .then(data => {
                matches = data;
                isLoadingMatches = false;
            });
        PlayerService.playerReadSeasons(data.id)
            .then(data => seasons = data);
        PlayerService.playerReadShots(data.id)
            .then(data => {
                shots = data;
                isLoadingShots = false;
            });
    })

</script>

<svelte:window bind:innerWidth={screenWidth} bind:innerHeight={screenHeight} />
<div class="!px-0" style="contain: paint;" bind:clientWidth={containerWidth}>
    <div class='bg-[#343a77] mb-16 relative z-50 lg:w-1/2'>
        <h1 class="text-6xl font-display font-bold text-stone-100">{data.player_name}</h1>
        <h2 class="text-md font-display text-stone-300 font-bold">The xG Story</h2>
    </div>

    {#if isLoadingShots}
        <p>Loading...</p>
    {:else}
        <div class='sticky top-[50%] -translate-y-1/2 lg:float-right' style='width: {width}px; height: {height}px' on:mouseleave={() => hoveredData = null}>
            <svg {width} {height} bind:this={svg}>
                <g transform='translate({margin.left}, {margin.top})'>
                    {#if currentStep == 0 || currentStep == undefined}
                        <Pitch width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} {shots} bind:tweenedX bind:tweenedY/>
                    {:else if currentStep == 1}
                        {#if !isLoadingMatches }
                            <Matches width={width - margin.left - margin.right} height={height - margin.top - margin.bottom} {matches} {shots}  bind:tweenedX bind:tweenedY/>
                        {/if}
                    {/if}
                
                {#each tweenedData as d, i}
                    <circle 
                        cx={d.x}
                        cy={d.y}
                        r={rScale(shots[i].xG)}
                        fill={(shots[i].result === 'Goal' ? "#00FF7F" : "#999999") + (hoveredData == null ? "aa" : hoveredData[1] == i ? "cc" : "33")}
                        stroke={"#000000" + (hoveredData == null ? "aa" : hoveredData[1] == i ? "cc" : "33")}
                        stroke-width=1
                        on:mouseover={() => {
                            hoveredData = [shots[i], i];
                        }}
                        on:focus={() => {
                            hoveredData = [shots[i], i];
                        }}
                        tabIndex="0"
                        style='transition: fill 300ms'
                    />
                {/each}
                </g>
            </svg>
            {#if hoveredData}
                <Tooltip shot={hoveredData[0]} index={hoveredData[1]} {tweenedX} {tweenedY} x={margin.left} y={margin.top} r={rScale(hoveredData[0].xG)} width={width-margin.right} {height} />
            {/if}
        </div>

        <Scrolly bind:value={currentStep}>
            {#each content as item, i}
                <div 
                    class='h-[85vh] flex place-items-center justify-center lg:block lg:w-3/5' 
                    class:active={currentStep === i}
                    >
                    <div 
                        class='p-8 w-full z-10 text-stone-100 font-display
                        {currentStep == i ? '' : ''}'
                        style='background: linear-gradient(0deg, #343a7733 0%, #343a77ee 20%, #343a77ee 80%, #343a7733 100%)'
                        >
                        <!-- <p class='text-stone-100 font-display'>{text}</p> -->
                        <svelte:component this={item} player={data} {shots} {matches}/>
                    </div>
                </div>
            {/each}
        </Scrolly>
    {/if}
</div>
