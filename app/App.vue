<template>

    <div id="app">
        <input v-model="searchProp" type="text" />
        <presence-list
            :students="students | searchParams(searchProp)">
        </presence-list>
    </div>

</template>

<script>
    import { presenceList } from './filter'

    export default {
        components: {
            presenceList
        },
        data() {
            return {
                searchProp: "",
                students: []
            }
        },
        filters: {
            searchParams
        }
    }

</script>
