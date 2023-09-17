<script lang="ts">
    import type { Shot } from '$client';
    export let data: Shot;
</script>

<p class="font-bold text-center">
    {`${data.h_team} ${data.h_goals} - ${data.a_goals} ${data.a_team}`.replaceAll(
        'rhampton Wanderers',
        's',
    )}
</p>
<p class="text-center mb-2 pb-2 border-b-[1px] border-slate-900">
    {new Date(data.date).toLocaleDateString()}
</p>
<div class="inline-block pr-2 pl-3 text-right text-slate-900">
    <p>Minute</p>
    <p>Situation</p>
    <p>Assist</p>
    <p>Shot type</p>
    <p>Result</p>
    <p>xG</p>
</div>
<div class="inline-block">
    <p>{data.minute}</p>
    <p>{data.situation.replace(/([A-Z])/g, ' $1').trim()}</p>
    <p>{data.player_assisted || '-'}</p>
    <p>{data.shotType.replace(/([A-Z])/g, ' $1').trim()}</p>
    <p>
        {data.result
            .replace(/([A-Z])/g, ' $1')
            .trim()
            .replace('Shots', 'Shot')}
    </p>
    <p>{data.xG.toFixed(2)}</p>
</div>
