<script>
    import Link from "./link.svelte";
</script>

<div class="flex justify-between items-center">
    <Link href="/">
        <h3><span class="text-4xl">&looparrowright;</span> RoundUp</h3>
    </Link>

    <nav class="w-1/2 flex justify-between">
        <Link href="how-it-works">How It Works</Link>
        <Link href="examples">Examples</Link>
        <Link href="sign-up" style="button">Sign Up</Link>
    </nav>
</div>
