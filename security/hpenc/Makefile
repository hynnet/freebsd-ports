# $FreeBSD$

PORTNAME=	hpenc
PORTVERSION=	1.0
PORTREVISION=	1
CATEGORIES=	security
MASTER_SITES=	http://highsecure.ru/distfiles/

MAINTAINER=	vsevolod@FreeBSD.org
COMMENT=	Fast authenticated encryption CLI tool

LICENSE=	BSD2CLAUSE

USES=		tar:xz compiler:c++11-lib gmake
USE_OPENSSL=	yes
PLIST_FILES=	bin/hpenc

MAKE_ARGS+=	"ARCH=${ARCH:S/amd64/x86/:S/i386/x86/}"
CXXFLAGS+=	-std=c++11 \
			-I${WRKSRC}/chacha-opt/app/include \
			-I${WRKSRC}/poly1305-opt/app/include
LDFLAGS+=	-pthread -lcrypto

.include <bsd.port.pre.mk>

.if ${OPSYS} == FreeBSD && ${OSVERSION} < 1000036
WITH_OPENSSL_PORT=	yes
.endif

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/hpenc

.include <bsd.port.post.mk>
