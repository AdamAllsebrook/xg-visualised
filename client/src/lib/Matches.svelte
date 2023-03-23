<script lang="ts">
    import type { Match, Shot } from '$client';
    import type { Spring } from 'svelte/motion';
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
    import { key as dataKey, type DataManager } from './data/dataManager';
    import { getContext } from 'svelte';
    
    export let width: number;
    export let height: number;
    export let tweenedX: Spring<number[]>;
    export let tweenedY: Spring<number[]>;
    
    const dataManager: DataManager = getContext(dataKey);
    const shots: Shot[] = dataManager.shots;
    const matches: Match[] = dataManager.matches;

    $: paddingY = height / (matches.length+1);
    $: matchesSorted = matches.sort((a, b) => Date.parse(a.date) - Date.parse(b.date));
    $: matchesMap = new Map(matchesSorted.map((match, i) => [match.id, i]));

    $: scale = (shot: Shot) => {
        return {
            x: Math.min(shot.minute, 90) * width / 90,
            y: (matchesMap.get(shot.match_id) || 0) * paddingY
        }
    }

    $: {scale; 
        tweenedX.set(shots.map(shot => scale(shot).x));
        tweenedY.set(shots.map(shot => scale(shot).y));
    }

</script>

<g  transition:fade="{{delay: 0, duration: 300, easing: cubicOut}}">
    {#each matchesSorted as match, i}
        <line
            x1=0
            x2={match.time_started * width / 90}
            y1={Math.round(i*paddingY)}
            y2={Math.round(i*paddingY)}
            stroke="#aaaaaa66"
            stroke-width=1
        />
        <rect
            x={match.time_started * width / 90}
            width={match.time * width / 90}
            y={Math.round(i*paddingY)-3}
            height=6
            rx=2
            stroke="black"
            stroke-width=1
            fill="#aaaaaa66"
        />
        <line
            x1={(match.time_started + match.time) * width / 90}
            x2={width}
            y1={Math.round(i*paddingY)}
            y2={Math.round(i*paddingY)}
            stroke="#aaaaaa66"
            stroke-width=1
        />
    {/each}
</g>
