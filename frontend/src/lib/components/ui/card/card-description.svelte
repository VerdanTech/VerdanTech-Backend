<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';
	import { cn } from '$lib/utils/shadcn.js';

	type $$Props = HTMLAttributes<HTMLParagraphElement>;

	let className: $$Props['class'] = undefined;
	export { className as class };
</script>

<p class={cn('text-sm text-neutral-11', className)} {...$$restProps}>
	<slot />
</p>
