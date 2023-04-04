<script lang='ts'>
    export let percentage: number;
    export let text: string;
</script>

<span style='margin-left: {percentage}%' />
<p class='inline-block -translate-x-1/2 text-white-800 pt-2'>{text}</p>
<div />
<span style='margin-left: {percentage}%' />
<p class='inline-block -translate-x-1/2 text-white-800'>v</p>
