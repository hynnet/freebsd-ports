# Created by: Antoine Brodin <antoine@FreeBSD.org>
# $FreeBSD$

PORTNAME=	pyelasticsearch
PORTVERSION=	1.0
CATEGORIES=	textproc python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	antoine@FreeBSD.org
COMMENT=	Flexible, high-scale API to elasticsearch

LICENSE=	BSD3CLAUSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}elasticsearch-py>=1.0.0:${PORTSDIR}/textproc/py-elasticsearch-py \
		${PYTHON_PKGNAMEPREFIX}simplejson>=3.0:${PORTSDIR}/devel/py-simplejson \
		${PYTHON_PKGNAMEPREFIX}six>=1.4.0:${PORTSDIR}/devel/py-six \
		${PYTHON_PKGNAMEPREFIX}urllib3>=1.8:${PORTSDIR}/net/py-urllib3

USES=		python
USE_PYTHON=	distutils autoplist

.include <bsd.port.mk>
