
async def test_read_banners(async_client, banner_schema, mocker):
    expected_result = [banner_schema.dict()]
    mocker.patch(
        'backend.foodcart.api.endpoints.banners.crud_banner.get_multi',
        return_value=[banner_schema],
    )

    response = await async_client.get('/api/banners/')

    assert response.status_code == 200
    assert response.json() == expected_result
