<script lang="ts">
    export let percentage: number;
    export let text: string;

    let height = 0;
</script>

<p
    class="absolute -translate-x-1/2 text-white-800 text-center"
    style="left: {percentage}%"
    bind:clientHeight={height}
>
    {text}<br /> v
</p>
<div class="mb-4" style="height: {height}px" />
