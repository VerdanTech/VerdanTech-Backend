<script lang="ts">
	import { Tabs as TabsPrimitive } from 'bits-ui';
	import { cn } from '$lib/utils/shadcn.js';

	type $$Props = TabsPrimitive.TriggerProps;
	type $$Events = TabsPrimitive.TriggerEvents;

	let className: $$Props['class'] = undefined;
	export let value: $$Props['value'];
	export { className as class };
</script>

<TabsPrimitive.Trigger
	class={cn(
		'inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-neutral-1 transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-neutral-11 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-neutral-1 data-[state=active]:text-neutral-11 data-[state=active]:shadow-sm',
		className
	)}
	{value}
	{...$$restProps}
	on:click
>
	<slot />
</TabsPrimitive.Trigger>
