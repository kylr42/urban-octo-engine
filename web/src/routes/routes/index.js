import DefaultLayout from '@/layouts/DefaultLayout.vue'

const routes = [
    {
        path: '/product/',
        name: 'product',
        component: () => import('@/views/Product.vue'),
        meta: {
            layout: DefaultLayout
        }
    },
]

export default routes