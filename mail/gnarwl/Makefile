# Created by: Xavier Beaudouin <kiwi@oav.net>
# $FreeBSD$

PORTNAME=	gnarwl
PORTVERSION=	3.6
PORTREVISION=	4
CATEGORIES=	mail
MASTER_SITES=	http://www.onyxbits.de/sites/default/files/

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Email autoresponder that gets data from LDAP

LIB_DEPENDS=	libgdbm.so:${PORTSDIR}/databases/gdbm
BUILD_DEPENDS=	${LOCALBASE}/bin/gsed:${PORTSDIR}/textproc/gsed

USES=		iconv gmake tar:tgz
USE_OPENLDAP=	yes
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-docdir=${DOCSDIR}

OPTIONS_DEFINE=	DOCS

.include <bsd.port.mk>
