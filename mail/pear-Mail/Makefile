# Created by: Thierry Thomas (<thierry@pompo.net>)
# $FreeBSD$

PORTNAME=	Mail
DISTVERSION=	1.2.0
PORTEPOCH=	1
CATEGORIES=	mail www pear

MAINTAINER=	ports@FreeBSD.org
COMMENT=	PEAR class that provides multiple interfaces for sending emails

OPTIONS_DEFINE=	PEAR_NET_SMTP
PEAR_NET_SMTP_DESC=	PEAR::Net_SMTP support

USES=	pear

PEAR_NET_SMTP_RUN_DEPENDS=	${PEARDIR}/Net/SMTP.php:${PORTSDIR}/net/pear-Net_SMTP

.include <bsd.port.mk>
