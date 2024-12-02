# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import demo_pb2 as demo__pb2


class CartServiceStub(object):
    """-----------------Cart service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddItem = channel.unary_unary(
                '/oteldemo.CartService/AddItem',
                request_serializer=demo__pb2.AddItemRequest.SerializeToString,
                response_deserializer=demo__pb2.Empty.FromString,
                )
        self.GetCart = channel.unary_unary(
                '/oteldemo.CartService/GetCart',
                request_serializer=demo__pb2.GetCartRequest.SerializeToString,
                response_deserializer=demo__pb2.Cart.FromString,
                )
        self.EmptyCart = channel.unary_unary(
                '/oteldemo.CartService/EmptyCart',
                request_serializer=demo__pb2.EmptyCartRequest.SerializeToString,
                response_deserializer=demo__pb2.Empty.FromString,
                )


class CartServiceServicer(object):
    """-----------------Cart service-----------------

    """

    def AddItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmptyCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CartServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=demo__pb2.AddItemRequest.FromString,
                    response_serializer=demo__pb2.Empty.SerializeToString,
            ),
            'GetCart': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCart,
                    request_deserializer=demo__pb2.GetCartRequest.FromString,
                    response_serializer=demo__pb2.Cart.SerializeToString,
            ),
            'EmptyCart': grpc.unary_unary_rpc_method_handler(
                    servicer.EmptyCart,
                    request_deserializer=demo__pb2.EmptyCartRequest.FromString,
                    response_serializer=demo__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.CartService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CartService(object):
    """-----------------Cart service-----------------

    """

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.CartService/AddItem',
            demo__pb2.AddItemRequest.SerializeToString,
            demo__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.CartService/GetCart',
            demo__pb2.GetCartRequest.SerializeToString,
            demo__pb2.Cart.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EmptyCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.CartService/EmptyCart',
            demo__pb2.EmptyCartRequest.SerializeToString,
            demo__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RecommendationServiceStub(object):
    """---------------Recommendation service----------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListRecommendations = channel.unary_unary(
                '/oteldemo.RecommendationService/ListRecommendations',
                request_serializer=demo__pb2.ListRecommendationsRequest.SerializeToString,
                response_deserializer=demo__pb2.ListRecommendationsResponse.FromString,
                )


class RecommendationServiceServicer(object):
    """---------------Recommendation service----------

    """

    def ListRecommendations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListRecommendations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRecommendations,
                    request_deserializer=demo__pb2.ListRecommendationsRequest.FromString,
                    response_serializer=demo__pb2.ListRecommendationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.RecommendationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecommendationService(object):
    """---------------Recommendation service----------

    """

    @staticmethod
    def ListRecommendations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.RecommendationService/ListRecommendations',
            demo__pb2.ListRecommendationsRequest.SerializeToString,
            demo__pb2.ListRecommendationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ProductCatalogServiceStub(object):
    """---------------Product Catalog----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListProducts = channel.unary_unary(
                '/oteldemo.ProductCatalogService/ListProducts',
                request_serializer=demo__pb2.Empty.SerializeToString,
                response_deserializer=demo__pb2.ListProductsResponse.FromString,
                )
        self.GetProduct = channel.unary_unary(
                '/oteldemo.ProductCatalogService/GetProduct',
                request_serializer=demo__pb2.GetProductRequest.SerializeToString,
                response_deserializer=demo__pb2.Product.FromString,
                )
        self.SearchProducts = channel.unary_unary(
                '/oteldemo.ProductCatalogService/SearchProducts',
                request_serializer=demo__pb2.SearchProductsRequest.SerializeToString,
                response_deserializer=demo__pb2.SearchProductsResponse.FromString,
                )


class ProductCatalogServiceServicer(object):
    """---------------Product Catalog----------------

    """

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductCatalogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=demo__pb2.Empty.FromString,
                    response_serializer=demo__pb2.ListProductsResponse.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=demo__pb2.GetProductRequest.FromString,
                    response_serializer=demo__pb2.Product.SerializeToString,
            ),
            'SearchProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchProducts,
                    request_deserializer=demo__pb2.SearchProductsRequest.FromString,
                    response_serializer=demo__pb2.SearchProductsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.ProductCatalogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductCatalogService(object):
    """---------------Product Catalog----------------

    """

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.ProductCatalogService/ListProducts',
            demo__pb2.Empty.SerializeToString,
            demo__pb2.ListProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.ProductCatalogService/GetProduct',
            demo__pb2.GetProductRequest.SerializeToString,
            demo__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.ProductCatalogService/SearchProducts',
            demo__pb2.SearchProductsRequest.SerializeToString,
            demo__pb2.SearchProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ShippingServiceStub(object):
    """---------------Shipping Service----------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetQuote = channel.unary_unary(
                '/oteldemo.ShippingService/GetQuote',
                request_serializer=demo__pb2.GetQuoteRequest.SerializeToString,
                response_deserializer=demo__pb2.GetQuoteResponse.FromString,
                )
        self.ShipOrder = channel.unary_unary(
                '/oteldemo.ShippingService/ShipOrder',
                request_serializer=demo__pb2.ShipOrderRequest.SerializeToString,
                response_deserializer=demo__pb2.ShipOrderResponse.FromString,
                )


class ShippingServiceServicer(object):
    """---------------Shipping Service----------

    """

    def GetQuote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShipOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShippingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetQuote': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQuote,
                    request_deserializer=demo__pb2.GetQuoteRequest.FromString,
                    response_serializer=demo__pb2.GetQuoteResponse.SerializeToString,
            ),
            'ShipOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.ShipOrder,
                    request_deserializer=demo__pb2.ShipOrderRequest.FromString,
                    response_serializer=demo__pb2.ShipOrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.ShippingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ShippingService(object):
    """---------------Shipping Service----------

    """

    @staticmethod
    def GetQuote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.ShippingService/GetQuote',
            demo__pb2.GetQuoteRequest.SerializeToString,
            demo__pb2.GetQuoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShipOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.ShippingService/ShipOrder',
            demo__pb2.ShipOrderRequest.SerializeToString,
            demo__pb2.ShipOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CurrencyServiceStub(object):
    """-----------------Currency service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSupportedCurrencies = channel.unary_unary(
                '/oteldemo.CurrencyService/GetSupportedCurrencies',
                request_serializer=demo__pb2.Empty.SerializeToString,
                response_deserializer=demo__pb2.GetSupportedCurrenciesResponse.FromString,
                )
        self.Convert = channel.unary_unary(
                '/oteldemo.CurrencyService/Convert',
                request_serializer=demo__pb2.CurrencyConversionRequest.SerializeToString,
                response_deserializer=demo__pb2.Money.FromString,
                )


class CurrencyServiceServicer(object):
    """-----------------Currency service-----------------

    """

    def GetSupportedCurrencies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Convert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CurrencyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSupportedCurrencies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSupportedCurrencies,
                    request_deserializer=demo__pb2.Empty.FromString,
                    response_serializer=demo__pb2.GetSupportedCurrenciesResponse.SerializeToString,
            ),
            'Convert': grpc.unary_unary_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=demo__pb2.CurrencyConversionRequest.FromString,
                    response_serializer=demo__pb2.Money.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.CurrencyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CurrencyService(object):
    """-----------------Currency service-----------------

    """

    @staticmethod
    def GetSupportedCurrencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.CurrencyService/GetSupportedCurrencies',
            demo__pb2.Empty.SerializeToString,
            demo__pb2.GetSupportedCurrenciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Convert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.CurrencyService/Convert',
            demo__pb2.CurrencyConversionRequest.SerializeToString,
            demo__pb2.Money.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class PaymentServiceStub(object):
    """-------------Payment service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Charge = channel.unary_unary(
                '/oteldemo.PaymentService/Charge',
                request_serializer=demo__pb2.ChargeRequest.SerializeToString,
                response_deserializer=demo__pb2.ChargeResponse.FromString,
                )


class PaymentServiceServicer(object):
    """-------------Payment service-----------------

    """

    def Charge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PaymentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Charge': grpc.unary_unary_rpc_method_handler(
                    servicer.Charge,
                    request_deserializer=demo__pb2.ChargeRequest.FromString,
                    response_serializer=demo__pb2.ChargeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.PaymentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PaymentService(object):
    """-------------Payment service-----------------

    """

    @staticmethod
    def Charge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.PaymentService/Charge',
            demo__pb2.ChargeRequest.SerializeToString,
            demo__pb2.ChargeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EmailServiceStub(object):
    """-------------Email service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendOrderConfirmation = channel.unary_unary(
                '/oteldemo.EmailService/SendOrderConfirmation',
                request_serializer=demo__pb2.SendOrderConfirmationRequest.SerializeToString,
                response_deserializer=demo__pb2.Empty.FromString,
                )


class EmailServiceServicer(object):
    """-------------Email service-----------------

    """

    def SendOrderConfirmation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmailServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendOrderConfirmation': grpc.unary_unary_rpc_method_handler(
                    servicer.SendOrderConfirmation,
                    request_deserializer=demo__pb2.SendOrderConfirmationRequest.FromString,
                    response_serializer=demo__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.EmailService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EmailService(object):
    """-------------Email service-----------------

    """

    @staticmethod
    def SendOrderConfirmation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.EmailService/SendOrderConfirmation',
            demo__pb2.SendOrderConfirmationRequest.SerializeToString,
            demo__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CheckoutServiceStub(object):
    """-------------Checkout service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PlaceOrder = channel.unary_unary(
                '/oteldemo.CheckoutService/PlaceOrder',
                request_serializer=demo__pb2.PlaceOrderRequest.SerializeToString,
                response_deserializer=demo__pb2.PlaceOrderResponse.FromString,
                )


class CheckoutServiceServicer(object):
    """-------------Checkout service-----------------

    """

    def PlaceOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CheckoutServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PlaceOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceOrder,
                    request_deserializer=demo__pb2.PlaceOrderRequest.FromString,
                    response_serializer=demo__pb2.PlaceOrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.CheckoutService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CheckoutService(object):
    """-------------Checkout service-----------------

    """

    @staticmethod
    def PlaceOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.CheckoutService/PlaceOrder',
            demo__pb2.PlaceOrderRequest.SerializeToString,
            demo__pb2.PlaceOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AdServiceStub(object):
    """------------Ad service------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAds = channel.unary_unary(
                '/oteldemo.AdService/GetAds',
                request_serializer=demo__pb2.AdRequest.SerializeToString,
                response_deserializer=demo__pb2.AdResponse.FromString,
                )


class AdServiceServicer(object):
    """------------Ad service------------------

    """

    def GetAds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAds': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAds,
                    request_deserializer=demo__pb2.AdRequest.FromString,
                    response_serializer=demo__pb2.AdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.AdService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdService(object):
    """------------Ad service------------------

    """

    @staticmethod
    def GetAds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.AdService/GetAds',
            demo__pb2.AdRequest.SerializeToString,
            demo__pb2.AdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FeatureFlagServiceStub(object):
    """------------Feature flag service------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFlag = channel.unary_unary(
                '/oteldemo.FeatureFlagService/GetFlag',
                request_serializer=demo__pb2.GetFlagRequest.SerializeToString,
                response_deserializer=demo__pb2.GetFlagResponse.FromString,
                )
        self.CreateFlag = channel.unary_unary(
                '/oteldemo.FeatureFlagService/CreateFlag',
                request_serializer=demo__pb2.CreateFlagRequest.SerializeToString,
                response_deserializer=demo__pb2.CreateFlagResponse.FromString,
                )
        self.UpdateFlag = channel.unary_unary(
                '/oteldemo.FeatureFlagService/UpdateFlag',
                request_serializer=demo__pb2.UpdateFlagRequest.SerializeToString,
                response_deserializer=demo__pb2.UpdateFlagResponse.FromString,
                )
        self.ListFlags = channel.unary_unary(
                '/oteldemo.FeatureFlagService/ListFlags',
                request_serializer=demo__pb2.ListFlagsRequest.SerializeToString,
                response_deserializer=demo__pb2.ListFlagsResponse.FromString,
                )
        self.DeleteFlag = channel.unary_unary(
                '/oteldemo.FeatureFlagService/DeleteFlag',
                request_serializer=demo__pb2.DeleteFlagRequest.SerializeToString,
                response_deserializer=demo__pb2.DeleteFlagResponse.FromString,
                )


class FeatureFlagServiceServicer(object):
    """------------Feature flag service------------------

    """

    def GetFlag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFlag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFlag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFlags(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFlag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FeatureFlagServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFlag,
                    request_deserializer=demo__pb2.GetFlagRequest.FromString,
                    response_serializer=demo__pb2.GetFlagResponse.SerializeToString,
            ),
            'CreateFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFlag,
                    request_deserializer=demo__pb2.CreateFlagRequest.FromString,
                    response_serializer=demo__pb2.CreateFlagResponse.SerializeToString,
            ),
            'UpdateFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFlag,
                    request_deserializer=demo__pb2.UpdateFlagRequest.FromString,
                    response_serializer=demo__pb2.UpdateFlagResponse.SerializeToString,
            ),
            'ListFlags': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFlags,
                    request_deserializer=demo__pb2.ListFlagsRequest.FromString,
                    response_serializer=demo__pb2.ListFlagsResponse.SerializeToString,
            ),
            'DeleteFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFlag,
                    request_deserializer=demo__pb2.DeleteFlagRequest.FromString,
                    response_serializer=demo__pb2.DeleteFlagResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'oteldemo.FeatureFlagService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FeatureFlagService(object):
    """------------Feature flag service------------------

    """

    @staticmethod
    def GetFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.FeatureFlagService/GetFlag',
            demo__pb2.GetFlagRequest.SerializeToString,
            demo__pb2.GetFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.FeatureFlagService/CreateFlag',
            demo__pb2.CreateFlagRequest.SerializeToString,
            demo__pb2.CreateFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.FeatureFlagService/UpdateFlag',
            demo__pb2.UpdateFlagRequest.SerializeToString,
            demo__pb2.UpdateFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFlags(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.FeatureFlagService/ListFlags',
            demo__pb2.ListFlagsRequest.SerializeToString,
            demo__pb2.ListFlagsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/oteldemo.FeatureFlagService/DeleteFlag',
            demo__pb2.DeleteFlagRequest.SerializeToString,
            demo__pb2.DeleteFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)