// plugins/api.ts
export default defineNuxtPlugin(() => {
  const authStore = useAuthStore()
  const config = useRuntimeConfig()

  const api = $fetch.create({
    baseURL: config.public.BACKEND_URL + '/api',
    onRequest({ options }) {
      const headers = new Headers(options.headers)
      if (authStore.accessToken) {
        headers.set('Authorization', `Bearer ${authStore.accessToken}`)
      }
      options.headers = headers
    },
    async onResponseError({ response }) {
      if (response.status === 401) {
        await authStore.fetchRefreshToken()
      }
    },
  })

  return {
    provide: {
      api,
    },
  }
})
