from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Population(db.Model):
    __tablename__ = 'population'
    pop_code = db.Column(db.String(10), primary_key=True)
    pop_name = db.Column(db.String(20))
    pop_description = db.Column(db.String(100))
    sup_code = db.Column(db.String(10))

class Samples(db.Model):
    __tablename__ = 'samples'
    s_id = db.Column(db.String(10), primary_key=True)
    pop_code = db.Column(db.String(10), db.ForeignKey('population.pop_code'))
    sup_code = db.Column(db.String(10))
    population = db.relationship('Population', backref='samples')

class Variant(db.Model):
    __tablename__ = 'variant'
    chromosome = db.Column(db.String(5))
    pos = db.Column(db.Integer)
    snpId = db.Column(db.String(50), primary_key=True)
    refe = db.Column(db.String(5))
    alt = db.Column(db.String(5))
    geneName = db.Column(db.String(50))

class PCA(db.Model):
    __tablename__ = 'pca'
    s_id = db.Column(db.String(10), db.ForeignKey('samples.s_id'), primary_key=True)
    PC1 = db.Column(db.Float(20))
    PC2 = db.Column(db.Float(20))

class AdmixtureQ(db.Model):
    __tablename__ = 'admixture_q'
    sample_id = db.Column(db.String(10), db.ForeignKey('samples.s_id'), primary_key=True)
    P1 = db.Column(db.Float(20))
    P2 = db.Column(db.Float(20))
    P3 = db.Column(db.Float(20))
    P4 = db.Column(db.Float(20))
    P5 = db.Column(db.Float(20))

class PopAlleleFrq(db.Model):
    __tablename__ = 'pop_allele_frq'
    chrom = db.Column(db.String(5))
    pos = db.Column(db.Integer)
    snpId = db.Column(db.String(50), db.ForeignKey('variant.snpId'), primary_key=True)
    refe = db.Column(db.String(5))
    alt = db.Column(db.String(5))
    geneName = db.Column(db.String(50))
    ACB_ref = db.Column(db.Float(20))
    ACB_alt = db.Column(db.Float(20))
    ASW_ref = db.Column(db.Float(20))
    ASW_alt = db.Column(db.Float(20))
    BEB_ref = db.Column(db.Float(20))
    BEB_alt = db.Column(db.Float(20))
    CDX_ref = db.Column(db.Float(20))
    CDX_alt = db.Column(db.Float(20))
    CEU_ref = db.Column(db.Float(20))
    CEU_alt = db.Column(db.Float(20))
    CHB_ref = db.Column(db.Float(20))
    CHB_alt = db.Column(db.Float(20))
    CHS_ref = db.Column(db.Float(20))
    CHS_alt = db.Column(db.Float(20))
    CLM_ref = db.Column(db.Float(20))
    CLM_alt = db.Column(db.Float(20))
    ESN_ref = db.Column(db.Float(20))
    ESN_alt = db.Column(db.Float(20))
    FIN_ref = db.Column(db.Float(20))
    FIN_alt = db.Column(db.Float(20))
    GBR_ref = db.Column(db.Float(20))
    GBR_alt = db.Column(db.Float(20))
    GIH_ref = db.Column(db.Float(20))
    GIH_alt = db.Column(db.Float(20))
    GWD_ref = db.Column(db.Float(20))
    GWD_alt = db.Column(db.Float(20))
    IBS_ref = db.Column(db.Float(20))
    IBS_alt = db.Column(db.Float(20))
    ITU_ref = db.Column(db.Float(20))
    ITU_alt = db.Column(db.Float(20))
    JPT_ref = db.Column(db.Float(20))
    JPT_alt = db.Column(db.Float(20))
    KHV_ref = db.Column(db.Float(20))
    KHV_alt = db.Column(db.Float(20))
    LWK_ref = db.Column(db.Float(20))
    LWK_alt = db.Column(db.Float(20))
    MSL_ref = db.Column(db.Float(20))
    MSL_alt = db.Column(db.Float(20))
    MXL_ref = db.Column(db.Float(20))
    MXL_alt = db.Column(db.Float(20))
    PEL_ref = db.Column(db.Float(20))
    PEL_alt = db.Column(db.Float(20))
    PJL_ref = db.Column(db.Float(20))
    PJL_alt = db.Column(db.Float(20))
    PUR_ref = db.Column(db.Float(20))
    PUR_alt = db.Column(db.Float(20))
    SIB_ref = db.Column(db.Float(20))
    SIB_alt = db.Column(db.Float(20))
    STU_ref = db.Column(db.Float(20))
    STU_alt = db.Column(db.Float(20))
    TSI_ref = db.Column(db.Float(20))
    TSI_alt = db.Column(db.Float(20))
    YRI_ref = db.Column(db.Float(20))
    YRI_alt = db.Column(db.Float(20))

class PopGenFrq(db.Model):
    __tablename__ = 'pop_gen_frq'
    chrom = db.Column(db.String(5))
    pos = db.Column(db.Integer)
    snpId = db.Column(db.String(50), db.ForeignKey('variant.snpId'), primary_key=True)
    refe = db.Column(db.String(5))
    alt = db.Column(db.String(5))
    geneName = db.Column(db.String(50))
    ACB_hom_alt = db.Column(db.Integer)
    ACB_het = db.Column(db.Integer)
    ACB_hom_ref = db.Column(db.Integer)
    ASW_hom_alt = db.Column(db.Integer)
    ASW_het = db.Column(db.Integer)
    ASW_hom_ref = db.Column(db.Integer)
    BEB_hom_alt = db.Column(db.Integer)
    BEB_het = db.Column(db.Integer)
    BEB_hom_ref = db.Column(db.Integer)
    CDX_hom_alt = db.Column(db.Integer)
    CDX_het = db.Column(db.Integer)
    CDX_hom_ref = db.Column(db.Integer)
    CEU_hom_alt = db.Column(db.Integer)
    CEU_het = db.Column(db.Integer)
    CEU_hom_ref = db.Column(db.Integer)
    CHB_hom_alt = db.Column(db.Integer)
    CHB_het = db.Column(db.Integer)
    CHB_hom_ref = db.Column(db.Integer)
    CHS_hom_alt = db.Column(db.Integer)
    CHS_het = db.Column(db.Integer)
    CHS_hom_ref = db.Column(db.Integer)
    CLM_hom_alt = db.Column(db.Integer)
    CLM_het = db.Column(db.Integer)
    CLM_hom_ref = db.Column(db.Integer)
    ESN_hom_alt = db.Column(db.Integer)
    ESN_het = db.Column(db.Integer)
    ESN_hom_ref = db.Column(db.Integer)
    FIN_hom_alt = db.Column(db.Integer)
    FIN_het = db.Column(db.Integer)
    FIN_hom_ref = db.Column(db.Integer)
    GBR_hom_alt = db.Column(db.Integer)
    GBR_het = db.Column(db.Integer)
    GBR_hom_ref = db.Column(db.Integer)
    GIH_hom_alt = db.Column(db.Integer)
    GIH_het = db.Column(db.Integer)
    GIH_hom_ref = db.Column(db.Integer)
    GWD_hom_alt = db.Column(db.Integer)
    GWD_het = db.Column(db.Integer)
    GWD_hom_ref = db.Column(db.Integer)
    IBS_hom_alt = db.Column(db.Integer)
    IBS_het = db.Column(db.Integer)
    IBS_hom_ref = db.Column(db.Integer)
    ITU_hom_alt = db.Column(db.Integer)
    ITU_het = db.Column(db.Integer)
    ITU_hom_ref = db.Column(db.Integer)
    JPT_hom_alt = db.Column(db.Integer)
    JPT_het = db.Column(db.Integer)
    JPT_hom_ref = db.Column(db.Integer)
    KHV_hom_alt = db.Column(db.Integer)
    KHV_het = db.Column(db.Integer)
    KHV_hom_ref = db.Column(db.Integer)
    LWK_hom_alt = db.Column(db.Integer)
    LWK_het = db.Column(db.Integer)
    LWK_hom_ref = db.Column(db.Integer)
    MSL_hom_alt = db.Column(db.Integer)
    MSL_het = db.Column(db.Integer)
    MSL_hom_ref = db.Column(db.Integer)
    MXL_hom_alt = db.Column(db.Integer)
    MXL_het = db.Column(db.Integer)
    MXL_hom_ref = db.Column(db.Integer)
    PEL_hom_alt = db.Column(db.Integer)
    PEL_het = db.Column(db.Integer)
    PEL_hom_ref = db.Column(db.Integer)
    PJL_hom_alt = db.Column(db.Integer)
    PJL_het = db.Column(db.Integer)
    PJL_hom_ref = db.Column(db.Integer)
    PUR_hom_alt = db.Column(db.Integer)
    PUR_het = db.Column(db.Integer)
    PUR_hom_ref = db.Column(db.Integer)
    SIB_hom_alt = db.Column(db.Integer)
    SIB_het = db.Column(db.Integer)
    SIB_hom_ref = db.Column(db.Integer)
    STU_hom_alt = db.Column(db.Integer)
    STU_het = db.Column(db.Integer)
    STU_hom_ref = db.Column(db.Integer)
    TSI_hom_alt = db.Column(db.Integer)
    TSI_het = db.Column(db.Integer)
    TSI_hom_ref = db.Column(db.Integer)
    YRI_hom_alt = db.Column(db.Integer)
    YRI_het = db.Column(db.Integer)
    YRI_hom_ref = db.Column(db.Integer)
