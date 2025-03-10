<script>
    import Footer from "./footer.svelte";
    import Header from "./header.svelte";
</script>

<div class="grid grid-rows-12 h-full">
    <div class="h-full items-top p-6">
        <Header></Header>
    </div>
    <div class="row-span-10 overflow-y-scroll">
        <slot></slot>
    </div>
    <Footer></Footer>
</div>
