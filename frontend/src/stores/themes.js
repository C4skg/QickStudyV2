import { defineStore } from "pinia";
import { getStorage,setStorage } from "@/utils/util";


export const themeStore = defineStore('theme',{
    state: ()=>{
        return {
            currentTheme: "sunlight",
            themes: {
                "sunlight": {
                    name: "日光",
                    config: {
                        
                    }
                },
                "moondark": {
                    name: "紫夜",
                    config: {}
                }
            }
        }
    },
    persist: {
        enabled: true,
        strategies: [
            {
                key: "theme",
                storage: localStorage,
                paths: ["currentTheme","themes"]
            }
        ]
    },
    getters: {
        getTheme(state){
            return state.themes
        }
    },
    actions: {

    }
})