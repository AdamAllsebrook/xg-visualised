<script lang='ts'>
    import { onMount } from 'svelte';
    import { ItemsService } from '$client';
    import type { PlayerSearch, TeamSearch } from '$client';

    let items: (PlayerSearch | TeamSearch)[]  = [];

    // load
    onMount(async () => {
        ItemsService.itemsRead()
            .then(data => items = data);
    });

	import { createCombobox } from 'svelte-headlessui';
	const combobox = createCombobox({ label: 'Players', selected: items[2] })

    $: filtered = items.filter(item => item.name.toLowerCase().replace(/\s+/g, '').includes($combobox.filter.toLowerCase().replace(/\s+/g, '')))
</script>