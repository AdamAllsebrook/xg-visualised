<script lang='ts'>
    import { colours } from '$lib/colours';

    export let id: number;
    export let cx: number;
    export let cy: number;
    export let r: number;
    export let highlight: boolean;
    export let faded: boolean;
    export let spotlight: boolean; 
    $: opacity = faded ? 0.3 : spotlight ? 0.9 : 0.8;
</script>

<circle
    {id}
    {cx}
    {cy}
    {r}
    fill={highlight ? colours.secondary : colours.grey}
    stroke={colours.black}
    fill-opacity={opacity}
    stroke-opacity={opacity}
    stroke-width=1
    tabIndex='0'
    style='transition: fill 300ms, fill-opacity 300ms'
    on:mouseover
    on:focus
    on:focusout
/>
